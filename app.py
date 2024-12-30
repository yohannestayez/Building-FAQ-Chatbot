from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

sys.path.append('services')
from gemini_llm import get_finance_faq_response

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Default route for health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Financial Advisor Chatbot!"})

# Chatbot route: Handles user queries
@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's query from the request
    user_query = request.json.get("query", "").strip()

    # Validate the input
    if not user_query:
        return jsonify({"error": "No query provided. Please provide a question."}), 400

    # Get the response from the Gemini LLM
    try:
        chatbot_response = get_finance_faq_response(user_query)
        return jsonify({"response": chatbot_response})
    except Exception as e:
        return jsonify({"error": f"Failed to process query: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
