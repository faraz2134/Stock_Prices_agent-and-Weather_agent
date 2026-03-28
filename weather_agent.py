import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

# --- THE WEATHER TOOL ---
def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    # 1. Use HTTPS
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    headers = {'User-Agent': 'Mozilla/5.0'} # Helps bypass some basic blocks
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            return f"The current temperature in {city} is {temp}°C."
        else:
            # This helps Gemini explain the EXACT error to you
            return f"Weather service error: {data.get('message', 'Unknown Error')}"
            
    except Exception as e:
        return f"Technical connection error: {e}"
# --- THE GEMINI CLIENT ---
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Use 2.5-flash for reliability while debugging
MODEL_ID = "models/gemini-2.5-flash"

def run_weather_agent(question):
    print(f"\nUser: {question}")
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=question,
            config={
                "tools": [get_weather],
                "automatic_function_calling": {"disable": False},
                "system_instruction": "You are a helpful weather assistant. Use the get_weather tool for all weather queries."
            }
        )
        print(f"Gemini: {response.text}")
    except Exception as e:
        print(f"Gemini Error: {e}")

# --- EXECUTION ---
if __name__ == "__main__":
    run_weather_agent("temperature of newyork and patna")