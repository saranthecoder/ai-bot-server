from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_response
import nltk

# Set NLTK data path explicitly
nltk.data.path.append('C:\\Users\\saran\\AppData\\Roaming\\nltk_data')

# Define a create_app function for initializing your Flask app
def create_app():
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

    return app  # Return the created app instance

# The following code should only be executed when this script is run directly
if __name__ == "__main__":
    app = create_app()  # Create the app using the create_app function
    app.run(debug=True)
