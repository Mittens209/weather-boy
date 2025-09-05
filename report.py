import os
import sys
import time
import threading
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

class LoadingAnimation:
    def __init__(self, message="Loading"):
        self.message = message
        self.is_running = False
        self.animation_thread = None

    def animate(self):
        dots = 1
        while self.is_running:
            sys.stdout.write('\r' + self.message + '.' * dots + ' ' * (3 - dots))
            sys.stdout.flush()
            dots = (dots + 1) % 4
            time.sleep(0.5)

    def start(self):
        self.is_running = True
        self.animation_thread = threading.Thread(target=self.animate)
        self.animation_thread.start()

    def stop(self):
        self.is_running = False
        if self.animation_thread:
            self.animation_thread.join()
        sys.stdout.write('\r' + ' ' * (len(self.message) + 3) + '\r')
        sys.stdout.flush()

def main():
    city = input("Enter the city name: ").strip()
    print()  # Add a blank line for spacing
    
    # Create and start the loading animation
    loading = LoadingAnimation("Generating weather report")
    loading.start()
    
    try:
        # Generate the report
        report = generate_weather_report(city)
    finally:
        # Stop the animation regardless of success or failure
        loading.stop()
    
    print("\n" + report)

if __name__ == "__main__":
    main()
