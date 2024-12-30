import requests

# Base URL of the Flask application
BASE_URL = "http://127.0.0.1:5000"

def test_chatbot(query):
    url = f"{BASE_URL}/chat"
    payload = {"query": query}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Query: {query}")
            print(f"Response: {response.json().get('response')}\n")
        else:
            print(f"Error {response.status_code}: {response.json().get('error')}")
    except Exception as e:
        print(f"Failed to connect to the chatbot API: {str(e)}")

def run_tests():
    # List of test queries
    test_queries = [
        "Can you explain compound interest?",
        "How does inflation impact savings?",
        "Tell me about budgeting tips.",
        "What are the risks of cryptocurrency?",
    ]
    
    print("Running chatbot tests...\n")
    for query in test_queries:
        test_chatbot(query)

if __name__ == "__main__":
    run_tests()
