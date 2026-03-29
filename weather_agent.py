import os
import requests
from dotenv import load_dotenv
from google import genai
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app)

# --- THE WEATHER TOOL ---
def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    headers = {'User-Agent': 'Mozilla/5.0'} 
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"The current temperature in {city} is {temp}°C with {desc}."
        else:
            return f"Weather service error: {data.get('message', 'Unknown Error')}"
            
    except Exception as e:
        return f"Technical connection error: {e}"

# --- THE GEMINI CLIENT ---
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

# Serve the Frontend
@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

# API Route for Chat
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_input,
            config={
                "tools": [get_weather],
                "automatic_function_calling": {"disable": False},
                "system_instruction": "You are a helpful weather assistant. Use the get_weather tool for all weather queries."
            }
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)