from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_response
import nltk
import os

# Specify the NLTK data directory path
nltk_data_dir = '/opt/render/nltk_data'  # Replace with the correct path

# Check if the specified path exists, if not, create it
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Set the NLTK data directory
nltk.data.path.append(nltk_data_dir)

# Download the 'punkt' data
nltk.download('punkt')


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if "message" in data:
            text = data["message"]
            response = get_response(text)
            message = {"answer": response}
            return jsonify(message)
        else:
            return jsonify({"error": "Missing 'message' in request JSON"}), 400
    except Exception as e:
    # Log the error for debugging
        print(f"An error occurred: {str(e)}")
    # Return an error response to the client
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)
