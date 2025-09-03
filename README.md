# 🌦️ Weather Reporter

An AI-powered CLI tool that generates **structured weather reports and actionable recommendations** for any city.  
Powered by **Moonshot Kimi K2** via **OpenRouter**.

---

## Features
- PAGASA-style weather bulletins
- Actionable recommendations for:
  - Public
  - Local government units (LGUs)
  - Fisherfolk & maritime activities
  - Schools & workplaces
- Uses `.env` for secure API key storage
- Simple CLI: just enter a city name

---

## Installation & Setup

```bash
# Clone the repo
git clone https://github.com/your-username/weather-reporter.git
cd weather-reporter

# (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install requests python-dotenv openai
