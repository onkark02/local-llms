# Harnessing Open Source LLMs and ChatGPT with Minimal Code

This repository contains various examples of how to use Open Source Large Language Models (LLMs) and ChatGPT with minimal code. It includes Python scripts for connecting to OpenAI APIs, models running on local servers powered by Ollama and LM Studio.

## Table of Contents

- [Usage](#usage)
  - [OpenAI API](#openai-api)
  - [Ollama](#ollama)
  - [LM Studio](#lm-studio)
- [Examples](#examples)
  - [OpenAI API Example](#openai-api-example)
  - [Ollama Example](#ollama-example)
  - [LM Studio Streaming Example](#lm-studio-streaming-example)


## Usage

### OpenAI API

To use the OpenAI API, you need to set up your API key and base URL. Update the `lmstudioendpoint.py` file with your API key and base URL.

### Ollama

To use Ollama, ensure you have the necessary setup and configurations. Refer to the `opensource_ollama.py` and `ollama_streamlit_ok.py` files for examples.

### LM Studio

To use LM Studio, ensure you have the necessary setup and configurations. Refer to the `lmstudioendpoint_streaming.py` file for an example of streaming responses.

## Examples

### OpenAI API Example

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="your-api-key")

completion = client.chat.completions.create(
    model="meta-llama-3.1-8b-instruct",
    messages=[
        {"role": "system", "content": "You are an expert in geography."},
        {"role": "user", "content": "Write a paragraph about the geography of the Deccan plateau."}
    ],
    temperature=0.1,
    stream=True
)

for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)#   l o c a l - l l m s  
 