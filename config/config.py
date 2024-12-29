from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('.env')

ALPHA_VANTAGE_API_KEY =os.getenv("ALPHA_VANTAGE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")