import google.generativeai as genai
import sys
sys.path.append("config")
from config import GEMINI_API_KEY


# Initialize the Gemini LLM client with the API key
genai.configure(api_key=GEMINI_API_KEY)

def get_finance_faq_response(question):
    # Read the base prompt from a text file
    try:
        with open("financial_prompt.md", "r") as file:
            base_prompt = file.read()
    except FileNotFoundError:
        return "The prompt file 'financial_prompt.txt' was not found. Please ensure it exists."

    # Combine the base prompt with the user's question
    custom_prompt = f"{base_prompt}\nQuestion: {question}"

    try:
        # Use the Gemini LLM to generate a response
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(custom_prompt)

        # Return the generated response text
        return response.text.strip()

    except Exception as e:
        return f"An error occurred while generating the response: {e}"
