from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Lagos"):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'

    weather_data = requests.get(url).json()
    return weather_data

if __name__ == "__main__":
    print("\n*** Get Weather Condition ***")
    city = input("Please enter a city name: ")
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)