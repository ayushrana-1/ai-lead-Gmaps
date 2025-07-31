import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from brain import ask_brain

# Define the message template
MESSAGE_TEMPLATE = """Hi [Recipient's Name],

I'm [Name], and I specialize in creating affordable, high-quality websites for businesses like yours using advanced AI technology. 🌐✨ With my expertise, I can help you establish a strong online presence that attracts more customers and enhances your brand image.

Here’s what you get for just \$170:
- Customizable Website Design 🎨
- Mobile-Friendly Layout 📱
- Fast Loading Speed for Optimal User Experience ⚡
- Responsive Layout 📱

Why Choose My Service?
- Fast Turnaround: Get your site live in just 48 hours! ⏰
- No Technical Skills Required: I handle everything for you. 🤝
- Affordable Pricing: High-quality websites without breaking the bank. 💰

If you're interested, just reply "YES" and I’ll send you more details and links to my already designed websites!

Best regards,
[Name]
Your Website Specialist"""


def setup_chrome_driver(download_dir):
    """Set up Chrome WebDriver with the specified download directory."""
    options = Options()
    options.add_argument("--headless")
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True
    }
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)


def download_file(driver, link, download_dir):
    """Download the file from the given link."""
    driver.get(link)
    time.sleep(5)  # Wait for download to complete

    files = os.listdir(download_dir)
    if not files:
        raise FileNotFoundError("No file downloaded.")
    return os.path.join(download_dir, files[0])


def process_content(content):
    """Process the downloaded content using the `ask_brain` function."""
    category_and_info = ask_brain(
        f"'{content}' this is the content scraped from Google Maps. Rearrange the clients' info in a well-mannered format including name, phone number, and website (write N/A if not available). At the beginning of the answer, write the category."
    )
    time.sleep(1)

    clients_without_website = ask_brain(
        f"'{category_and_info}' First, write the category at the top. Then, extract the clients who don't have a website, along with their name and phone number."
    )
    time.sleep(1)

    messages = ask_brain(
        f"'{clients_without_website}' These are the client infos without a website. Write a short WhatsApp message for each of them like this: '{MESSAGE_TEMPLATE}'. You can also change it as per the client category. Write for each one by one, and at the end of each client's message, provide their phone number (the number should not be included in the message)."
    )
    return messages


def main():
    query = input("Write the Category + Place: ")
    link = f"https://www.google.com/search?gl=in&tbm=map&q{query}=&pb=!4m8!1m3!1d41630954.643199906!2d-119.5320212!3d34.29011580000001!3m2!1i1210!2i1184!4f13.1!7i20!10b1!12m16!1m2!18b1!30b1!17m4!1e1!1e0!3e1!3e0!20m6!1e0!2e3!3b0!5e2!6b1!8b1!26b1!19m4!2m3!1i320!2i120!4i8!20m32!3m1!2i9!6m3!1m2!1i360!2i256!7m24!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!9b0!22m7!4m1!2i22236!7e140!9sbcyFaO2LOvWdseMP6ZGUaA%3A350868209728!17sbcyFaO2LOvWdseMP6ZGUaA%3A350868209729!24m1!2e1!24m39!1m2!18m1!17b1!4b1!11m2!3e1!3e0!17b1!20m2!1e3!1e1!24b1!29b1!72m18!1m8!2b1!5b1!7b1!12m4!1b1!2b1!4m1!1e1!4b0!8m6!1m2!4m1!1e1!3sother_user_google_review_posts!6m1!1e1!9b1!89b1!98m3!1b1!2b1!3b1!122m1!1b1!26m7!1e12!1e15!1e13!1e3!2m2!1i80!2i80!34m5!9b1!12b1!14b1!25b1!26b1!37m1!1e140!49m5!6m2!1b1!2b1!8b1!10e11!69i741"

    # Set up download directory
    download_dir = os.path.join(os.getcwd(), "gmaps_download")
    os.makedirs(download_dir, exist_ok=True)

    # Set up Chrome driver and download the file
    driver = setup_chrome_driver(download_dir)
    try:
        filepath = download_file(driver, link, download_dir)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process the content and generate messages
        messages = process_content(content)

        # Save the messages to a file
        with open("client_info.txt", "w", encoding="utf-8") as f:
            f.write(messages)
        print("Done👍")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
