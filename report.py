import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in .env file.")

# Initialize OpenAI client pointing to OpenRouter
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_weather_report(city: str) -> str:
    """
    Generates a weather-style report with recommendations using Kimi K2 via OpenRouter.
    """
    prompt = f"""Please generate a professional-format weather report for {city}, including:
- Weather conditions
- Temperature
- Rainfall / flood risk
- Sea conditions (if relevant)
Then provide recommendations for:
1. The general public
2. Local government units (LGUs)
3. Fisherfolk & maritime activities
4. Schools and workplaces
"""

    response = client.chat.completions.create(
        model="moonshotai/kimi-k2:free",
        messages=[
            {"role": "system", "content": "You are a skilled meteorological assistant drafting weather bulletins."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content

def main():
    city = input("Enter the city name: ").strip()
    print("\nGenerating weather report…\n")
    report = generate_weather_report(city)
    print(report)

if __name__ == "__main__":
    main()
