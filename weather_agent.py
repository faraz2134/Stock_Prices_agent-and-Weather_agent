from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- WEATHER TOOL ---
def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"{city}: {temp}°C, {desc}"
        else:
            return f"Error: {data.get('message')}"
    except Exception as e:
        return f"Error: {e}"

# --- GEMINI CLIENT ---
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

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
                "system_instruction": "You are a weather assistant. Always use get_weather tool for weather queries."
            }
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)