import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.Client()

messages = [
    {"role": "user", "content": "List 3 reasons why strength training is healthy"}
]

result = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

print(result)
print("------------------------------")
print(result.choices[0].message.content)
