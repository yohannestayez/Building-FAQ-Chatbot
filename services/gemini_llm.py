import google.generativeai as genai
import sys
sys.path.append("config")
sys.path.append('services')
from alpha_vantage import get_stock_price
from config import GEMINI_API_KEY


# Initialize the Gemini LLM client with the API key
genai.configure(api_key=GEMINI_API_KEY)

def get_finance_faq_response(question):
    """
    Handles finance-related questions by identifying stock-related terms using an LLM
    and fetching stock data using the Alpha Vantage API only for explicitly stock-related queries.

    :param question: str, the user's question
    :return: str, the generated response or stock data
    """
    # Predefined stock-related keywords
    stock_symbols = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "INTC", "CSCO", "DIS", 
        "IBM", "CRM", "PYPL", "NFLX", "ADBE", "COST", "SBUX", "MCD", "NKE", "HD", 
        "LOW", "T", "VZ", "DISH", "GM", "F", "BA", "UNP", "CSX", "UPS", "FDX", "PG", 
        "KO", "PEP", "WMT", "TGT", "JPM", "BAC", "WFC", "C", "GS", "MS", "V", "MA", 
        "JNJ", "PFE", "UNH", "MRK", "ABT", "LLY", "CVS", "XOM", "CVX", "SLB", "COP", 
        "EOG", "BHP", "RIO", "GOLD", "NEM"
    ]

# Assuming `question` is provided
    try:
        # Improved prompt for stock-related intent analysis
        analysis_prompt = (
            f"Analyze the following question to determine if it relates to stock markets or specific stock symbols. "
            f"Check if the question contains any references to stock symbols from the following list: {', '.join(stock_symbols)}. "
            f"Return 'True' if the question has any of the symbols from the list, or 'False' if it is not. "
            f"Question: \"{question}\""
        )
        model = genai.GenerativeModel("gemini-1.5-flash")
        analysis_response = model.generate_content(analysis_prompt)
        analysis_result = analysis_response.text.strip().lower()
        
        # Parse the model's response to determine if stock-related terms were found
        if 'true' in analysis_result:
            is_stock_related = True
        else:
            is_stock_related = False
    except Exception as e:
        return f"An error occurred during analysis: {str(e)}"

    if is_stock_related:
        # Attempt to extract a potential stock symbol from the question
        words = question.split()
        stock_symbol = next(
            (word for word in words if word.isupper() and 1 <= len(word) <= 5),
            None
        )
        if stock_symbol:
            # Fetch stock data for valid stock symbol
            try:
                stock_data = get_stock_price(stock_symbol)
                return f"Stock data for {stock_symbol}: {stock_data}"
            except Exception as e:
                return f"Sorry, I couldn't fetch stock data for {stock_symbol}: {str(e)}"
        else:
            return "The question seems stock-related, but I couldn't identify a valid stock symbol."
    
    # Handle non-stock-related finance questions
    try:
        with open("financial_prompt.md", "r") as file:
            base_prompt = file.read()
    except FileNotFoundError:
        return "The prompt file 'financial_prompt.md' was not found. Please ensure it exists."

    # Combine the base prompt with the user's question
    custom_prompt = f"{base_prompt}\nQuestion: {question}"

    try:
        # Generate a response using the Gemini LLM
        response = model.generate_content(custom_prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating the response: {str(e)}"
