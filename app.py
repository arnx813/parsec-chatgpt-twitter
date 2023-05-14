from flask import Flask, request

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def endpoint():
    data = request.json  # Access the JSON data sent in the request
    # Process the data or perform any desired operations here
    print(data)  # Example: Print the data to the console

    # Return a response if needed
    response = {'message': 'Request received successfully'}
    return response, 200

def print_app_info():
    print("Flask app is live and running!")

if __name__ == '__main__':
    print_app_info()
    app.run(host='0.0.0.0', port=5001)
