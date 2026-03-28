import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="who r u?",
    config={
                'system_instruction': "You are a helpful coding assistant who explains simply."
            }
)

print(response.text)