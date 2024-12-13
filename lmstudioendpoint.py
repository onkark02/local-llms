# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    #model="meta-llama-3.1-8b-instruct",
    model="llama-3.2-1b-instruct",
    messages=[
        {"role": "system", "content": "You are an expert in geography."},
        {
            "role": "user",
            "content": "Which are the largest rivers in the european continent?",
        }
    ],
    temperature=0.1
)


#print the response
print(completion.choices[0].message.content)