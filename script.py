import os
import openai

openai.api_key = "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"

print(openai.api_key)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)
print('test')