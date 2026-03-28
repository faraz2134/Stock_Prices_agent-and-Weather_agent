import os
import dotenv
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
# --- THE STOCK PRICES TOOL ---
def get_stock_price(ticker: str) -> str:
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    
    headers = {'User-Agent': 'Mozilla/5.0'} # Helps bypass some basic blocks
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            price = data["Global Quote"]["05. price"]
            return f"The current stock price of {ticker} is ${price}."
        else:
            return f"Stock service error: {data.get('Note', 'Unknown Error')}"
            
    except Exception as e:
        return f"Technical connection error: {e}"
    
# --- THE GEMINI CLIENT ---
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"
def run_stock_agent(question):
    print(f"\nUser: {question}")
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=question,
            config={
                "tools": [get_stock_price],
                "automatic_function_calling": {"disable": False},
                "system_instruction": "You are a helpful stock price assistant. Use the get_stock_price tool for all stock price queries."
            }
        )
        print(f"Gemini: {response.text}")
    except Exception as e:
        print(f"Gemini Error: {e}")
if __name__ == "__main__":
      run_stock_agent("What is the stock price of AAPL?")
