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
        print('i received this json request from parsec, a crypto analytics platform. please convert this json response an understandable tweet. in ur response, do not provide any other text, only the tweet\n', data)  # Example: Print the data to the console
        chatbot_completion("asdfasdf")

        # Return a response if needed
        response = {'message': 'Request received successfully'}
        return jsonify(response), 200

def print_app_info():
    print("Flask app is live and running!")

if __name__ == '__main__':
    print_app_info()
    app.run(host='0.0.0.0', port=5001)
