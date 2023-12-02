import os
import openai

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")

def gpt(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=1000, n=1, stop=None):
    messages = [{"role": "user", "content": prompt}]
    global completion_tokens, prompt_tokens
    outputs = []
    while n > 0:
        cnt = min(n, 20)
        n -= cnt
        res = openai.ChatCompletion.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens, n=cnt, stop=stop)
        outputs.extend([choice["message"]["content"] for choice in res["choices"]])
    return outputs