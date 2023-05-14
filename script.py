import openai

def chatbot_completion(message):
    openai.api_key = "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"

    print(openai.api_key)

    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": message}
    #     ]
    # )

    # print(completion.choices[0].message.content)

# Call the function and pass a message as a parameter
# chatbot_completion("tell me about your self.")
