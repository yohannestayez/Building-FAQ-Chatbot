import requests
import sys
sys.path.append("C:/Users/Administrator/Documents/Icog/Code/Financial-chatbot/config")
from config import ALPHA_VANTAGE_API_KEY

def get_stock_price(symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "Time Series (1min)" in data:
        latest_time = list(data["Time Series (1min)"].keys())[0]
        stock_price = data["Time Series (1min)"][latest_time]["1. open"]
        return f"The latest stock price for {symbol} is ${stock_price}"
    else:
        return "Sorry, I couldn't fetch the stock price. Please check the ticker symbol or try again later."
