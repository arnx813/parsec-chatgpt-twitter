import openai
import os

def chatbot_completion(message):
    # api_key = os.environ.get('OPENAI_API_KEY')

    api_key = os.environ["OPENAI_API_KEY"]
    print(api_key)


    print(message)

    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": message}
    #     ]
    # )

    # print(completion.choices[0].message.content)

# Call the function and pass a message as a parameter
# chatbot_completion("tell me about your self.")
