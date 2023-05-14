from flask import Flask, request, jsonify
from twitter import create_tweet
from script import chatbot_completion

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the home endpoint!'})

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        data = request.json
        chatgpt_tweet = chatbot_completion('i received this json from parsec, a crypto analytics platform. i am converting this json data into a tweet that alerts users of important transactions that are happening in DeFi. i am posting this tweet on a parody sam bankman fried twitter account. could you provide me a tweet to use, written in an over-the-top nerdy and geeky tone, under 200 characters? ' + str(data))
        print(chatgpt_tweet)
        create_tweet(chatgpt_tweet)

        # Return a response if needed
        response = {'message': 'Request received successfully'}
        return jsonify(response), 200

def print_app_info():
    print("Flask app is live and running!")

if __name__ == '__main__':
    print_app_info()
    app.run(host='0.0.0.0', port=5001)
