# ai-lead-Gmaps
# Google Maps Scraper and Client Outreach Tool

This Python script automates the process of scraping business information from Google Maps and generating personalized WhatsApp messages for outreach. It leverages Selenium for web scraping and a custom `ask_brain` function (from the `brain` module) to process and organize the scraped data.

## Features
- **Google Maps Scraping**: Automatically scrapes business information based on a user-provided category and location.
- **Data Processing**: Processes the scraped data to extract client names, phone numbers, and websites.
- **Message Generation**: Creates personalized WhatsApp messages for clients without websites.
- **File Saving**: Saves the generated messages to a `client_info.txt` file for easy access.

## Prerequisites
Before running the script, ensure you have the following installed:
1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
