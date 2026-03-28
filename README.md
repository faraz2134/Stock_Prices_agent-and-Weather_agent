# 🌦️ Agentic AI: Weather & Stock Price Assistant

An intelligent, tool-augmented assistant built with the Google Gemini SDK. This agent doesn't just chat—it decides when to use external APIs to fetch real-time weather and stock data.

---

## 🚀 Features

* 🧠 **Natural Language Understanding** using Gemini Flash models
* 🛠 **Function Calling** (tool usage like real agents)
* 🌦 **Real-time Weather Data** via OpenWeatherMap
* 📈 **Stock Price Fetching** (e.g., NVDA, TSLA)
* ⚡ **Error Handling** with retry logic for `503` and `429` errors

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd your-project-folder
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Activate:

**Windows**

```bash
.\venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -U google-genai python-dotenv requests
```

---

### 4. Configure Environment Variables

Create a `.env` file in root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
OPENWEATHER_API_KEY=your_openweathermap_key_here
ALPHA_VANTAGE_API_KEY=your_stock_api_key_here
```

⚠️ Never push `.env` to GitHub

---

## 📂 Project Structure

```
project/
│── main.py        # Core agent logic
│── tools.py       # External API tools (weather, stock)
│── .env           # API keys (ignored)
│── .gitignore
```

---

## 🤖 How the Agent Works

This project uses a **ReAct (Reason + Act) loop**:

1. User asks a question
2. Gemini decides if a tool is needed
3. Tool executes (weather / stock API)
4. Result sent back to Gemini
5. Gemini returns final natural response

---

## ⚠️ Troubleshooting

### ❌ Invalid API Key

* OpenWeather keys may take **1–2 hours** to activate

### ❌ 503 Errors

* Caused by high load on Gemini models
* Retry logic already handled in code

### ❌ Accidentally pushed `.env`

```bash
git rm -r --cached .env
```

---

## 🚀 Future Improvements

* 🔁 Add conversation memory
* 🌐 Add web search tool
* 🗣 Voice input/output
* 🤖 Fully autonomous agent loop

---

## ⭐ Contribute

Feel free to fork, improve, and build your own agentic systems 🚀
