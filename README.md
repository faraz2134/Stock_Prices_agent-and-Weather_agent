# 🌦️ Agentic AI: Weather & Stock Price Assistant

An intelligent, tool-augmented assistant built with the Google Gemini 2026 SDK. This agent doesn't just "chat"—it decides when to use external APIs to fetch real-time weather and financial data.

## 🚀 Features
- **Natural Language Understanding**: Uses Gemini 2.5/3.0 Flash for reasoning and intent detection.
- **Function Calling**: Automatically triggers local Python functions based on user requests.
- **Real-time Weather**: Integrated with the OpenWeatherMap API.
- **Stock Market Data**: Built-in support for fetching ticker prices (e.g., NVDA, TSLA).
- **Error Handling**: Includes exponential backoff for `503 Service Unavailable` and `429 Rate Limit` errors.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd your-project-folder

Gemini said
A professional README.md is the "front door" of your project. Since you are building an AI Agent that uses Gemini 3 Flash (or 2.5 Flash) and external tools, your README should clearly explain how to set up the environment and the API keys.

Here is a complete, well-formatted README.md file for your project.

README.md
Markdown
# 🌦️ Agentic AI: Weather & Stock Price Assistant

An intelligent, tool-augmented assistant built with the Google Gemini 2026 SDK. This agent doesn't just "chat"—it decides when to use external APIs to fetch real-time weather and financial data.

## 🚀 Features
- **Natural Language Understanding**: Uses Gemini 2.5/3.0 Flash for reasoning and intent detection.
- **Function Calling**: Automatically triggers local Python functions based on user requests.
- **Real-time Weather**: Integrated with the OpenWeatherMap API.
- **Stock Market Data**: Built-in support for fetching ticker prices (e.g., NVDA, TSLA).
- **Error Handling**: Includes exponential backoff for `503 Service Unavailable` and `429 Rate Limit` errors.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd your-project-folder

2. Create a Virtual Environment
It is highly recommended to use a venv to manage dependencies.
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -U google-genai python-dotenv requests

4. Configure Environment Variables
Create a file named .env in the root directory. Never commit this file to GitHub.

GOOGLE_API_KEY=your_gemini_api_key_here
OPENWEATHER_API_KEY=your_openweathermap_key_here
ALPHA_VANTAGE_API_KEY=Your_api_key

Gemini said
A professional README.md is the "front door" of your project. Since you are building an AI Agent that uses Gemini 3 Flash (or 2.5 Flash) and external tools, your README should clearly explain how to set up the environment and the API keys.

Here is a complete, well-formatted README.md file for your project.

README.md
Markdown
# 🌦️ Agentic AI: Weather & Stock Price Assistant

An intelligent, tool-augmented assistant built with the Google Gemini 2026 SDK. This agent doesn't just "chat"—it decides when to use external APIs to fetch real-time weather and financial data.

## 🚀 Features
- **Natural Language Understanding**: Uses Gemini 2.5/3.0 Flash for reasoning and intent detection.
- **Function Calling**: Automatically triggers local Python functions based on user requests.
- **Real-time Weather**: Integrated with the OpenWeatherMap API.
- **Stock Market Data**: Built-in support for fetching ticker prices (e.g., NVDA, TSLA).
- **Error Handling**: Includes exponential backoff for `503 Service Unavailable` and `429 Rate Limit` errors.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd your-project-folder
2. Create a Virtual Environment
It is highly recommended to use a venv to manage dependencies.

Bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -U google-genai python-dotenv requests
4. Configure Environment Variables
Create a file named .env in the root directory. Never commit this file to GitHub.

Code snippet
GOOGLE_API_KEY=your_gemini_api_key_here
OPENWEATHER_API_KEY=your_openweathermap_key_here
📂 Project Structure
main.py: The core agent logic and Gemini client setup.

tools.py: (Optional) If you choose to move your tool functions to a separate file.

.env: Stores your private API credentials.

.gitignore: Configured to ignore venv/, __pycache__/, and .env.

🤖 How the Agent Works
The agent follows a "Reasoning and Acting" (ReAct) loop:

User Prompt: "What is the temperature in New Delhi?"

Model Decision: Gemini identifies that it needs the get_weather tool.

Execution: The Python SDK executes the function locally and sends the result back to Gemini.

Final Response: Gemini formats the raw data into a friendly, natural sentence.

⚠️ Troubleshooting
Invalid API Key: If using OpenWeatherMap, new keys can take up to 2 hours to activate.

503 Errors: This indicates high demand on Google's preview models. The script includes a retry loop to handle this.

Git Safety: Ensure you run git rm -r --cached .env if you accidentally committed your keys previously.
