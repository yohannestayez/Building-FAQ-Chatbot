from flask import Flask, request, jsonify
import sys

sys.path.append('services')
from gemini_llm import get_finance_faq_response
from alpha_vantage import get_stock_price



app = Flask(__name__)




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

# Stock data route: Fetches stock information
@app.route('/stock', methods=['POST'])
def stock():
    # Get the stock symbol from the request
    stock_symbol = request.json.get("symbol", "").strip()

    # Validate the input
    if not stock_symbol:
        return jsonify({"error": "No stock symbol provided. Please provide a valid stock ticker symbol."}), 400

    # Get the stock data from Alpha Vantage
    try:
        stock_data = get_stock_price(stock_symbol)
        return jsonify({"stock_data": stock_data})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch stock data: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
