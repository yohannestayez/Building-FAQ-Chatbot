# Financial Advisor Chatbot

## Overview
The **Financial Advisor Chatbot** is a simple, interactive chatbot designed to provide financial guidance by answering frequently asked questions about finance. It leverages **Gemini LLM** for generating responses and integrates **Alpha Vantage API** to fetch real-time financial data. 

## Features
- User-friendly interface built with HTML, CSS, and JavaScript.
- Answers FAQs using Gemini LLM (free version).
- Fetches stock and financial data using Alpha Vantage API.
- Fully functional backend developed in Flask.


## Folder Structure
```
.
├── .github            
│   └── workflows
│       └── unittests.yml
├── config              # Configuration files
│   └── config.py
├── Frontend            # Frontend files
│   ├── index.html      # Chatbot UI
│   ├── README.md       # Frontend details
│   ├── scripts.js      # Frontend logic and API calls
│   └── style.css       # Styling for the chatbot
├── Screenshots         # Screenshots of the chatbot in action
│   ├── Screenshot 1.png
│   └── Screenshot 2.png
├── services            # Backend services
│   ├── alpha_vantage.py  # Alpha Vantage integration
│   ├── gemini_llm.py     # Gemini LLM integration
│   └── README.md         # Backend services details
├── tests               
│   └── test_chatbot.py  # Test script
├── .gitignore          # Git ignore file
├── app.py              # Main Flask application
├── financial_prompt.md # Financial FAQ prompts for the chatbot
├── README.md           # README file
└── requirements.txt    # Python dependencies
```

### Project Dependencies

This project relies on the following Python libraries:

* `Flask`
* `requests`
* `google-generativeai`

## Installation

### Prerequisites
- Python 3.8+
- Flask
- Gemini API key
- Alpha Vantage API key

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yohannestayez/Building-FAQ-Chatbot.git
   ```
2. Navigate to the project directory:

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your API keys to the `.env` file:

   ```
   GEMINI_API_KEY= "your gemini api key"
   ALPHA_VANTAGE_API_KEY= "your alpha vantage api key"
   ```
5. Run the Flask application:

   ```
   python app.py
   ```
6. Open the chatbot in your browser at `http://127.0.0.1:5500/Frontend/index.html`.

## Usage
- Access the chatbot UI via the provided frontend.
- Type your financial queries in the input box and press "Send" or hit "Enter".
- The chatbot will fetch responses using Gemini LLM and Alpha Vantage APIs.

## Testing
Run the unit tests to ensure everything works correctly:

```
python tests/test_chatbot.py
```

## Acknowledgments
- [Gemini LLM](https://cloud.google.com/gen-ai/) for natural language processing and chat Responses.
- [Alpha Vantage](https://www.alphavantage.co/) for financial data.
