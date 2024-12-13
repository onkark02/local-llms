import dotenv
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client()

messages = [
    {
        "role": "user",
        "content": "List the benefits of fibers in the diet"
    }
]
model = 'gpt-3.5-turbo-1106'
result = client.chat.completions.create(model=model, messages=messages, stream=True)

for chunk in result:
    print(chunk.choices[0].delta.content, end="", flush=True)
