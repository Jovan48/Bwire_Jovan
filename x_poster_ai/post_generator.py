import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic: str) -> str:
    prompt = f"Create a short, engaging Twitter post about: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response['choices'][0]['message']['content']
    return message.strip()
