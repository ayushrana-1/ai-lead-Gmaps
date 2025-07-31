from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def ask_brain(query):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response.choices[0].message.content
