# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="meta-llama-3.1-8b-instruct",
    messages=[
        {"role": "system", "content": "You are an expert in geography."},
        {
            "role": "user",
            "content": "Write a paragraph about the geography of the Deccan plateau.",
        }
    ],
    temperature=0.1,
    stream=True
)

# print the streaming response
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)
