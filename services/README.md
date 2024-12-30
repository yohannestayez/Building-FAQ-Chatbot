## alpha_vantage.py
-   This script fetches the latest stock price for a given symbol using the Alpha Vantage API. It retrieves intraday data at a 1-minute interval and returns the latest opening price. If the request fails or the symbol is incorrect, an error message is returned.

## gemini_llm.py
-   This script uses the Gemini LLM and Alpha Vantage API to handle finance-related questions. If a question is stock-related (based on predefined stock symbols), it fetches the latest stock price using the Alpha Vantage API. For non-stock-related finance questions, it generates a response using a predefined prompt and the Gemini LLM. If any errors occur during analysis or data retrieval, appropriate error messages are returned.