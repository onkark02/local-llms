# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

while True:
    prompt = input("\nAsk your question: \n")
    completion = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": "You are an assistant who answers politely."},
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.7,
        stream=True
    )

    # print the streaming response
    for chunk in completion:
        print(chunk.choices[0].delta.content, end="", flush=True)
