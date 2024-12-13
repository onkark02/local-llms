import json
import openai
import os
from dotenv import load_dotenv

import yfinance as yf

def get_price(ticker):
    tk = yf.Ticker(ticker)
    return json.dumps(tk.info.get('currentPrice'))

def start(message):
    print("Message: ", message)
    m = {"role": "user", "content": message}
    messages.append(m)
    result = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, functions = func)
    return result.choices[0].message


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a stockbroker returning prices of stocks."},
]

func = [
    {
        "name": "get_price",
        "description": "Returns the current price of a stock ticker",
        "parameters": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "The stock ticker symbol for which current price is required"
                }
            },
            "required": ["ticker"]
        }
    }
]

client = openai.Client()

question = "what are the stock prices of microsoft and nvidia?"
model_answer = start(question)
print("Model Answer: ", model_answer)
if model_answer.function_call:
    arguments = json.loads(model_answer.function_call.arguments).get('ticker')
    function_name = model_answer.function_call.name
    final_result = eval(f"{function_name}('{arguments}')")
    print(final_result)
else:
    print(model_answer.content)


