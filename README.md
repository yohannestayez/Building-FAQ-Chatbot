## app.py
- This script sets up a Flask web application that serves as a Financial Advisor Chatbot. It defines two routes: a default health check route (/) that returns a welcome message, and a /chat route that processes user queries. The chatbot route receives a query from the user, validates it, and passes it to the get_finance_faq_response function from the gemini_llm module for a response. If the input is valid, the chatbot's response is returned as JSON. If an error occurs, an error message is sent in the response.
## financial_prompt.md
- This is the prompt given to the llm.