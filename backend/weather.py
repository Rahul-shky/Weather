from asyncio.windows_events import NULL
import requests
import os
from dotenv import load_dotenv
import json
from dataclasses import dataclass

load_dotenv()
API_key = os.getenv("API_key")


@dataclass
class weather:
    main: str
    description: str
    icon: str
    temperature: float
    pressure: int
    humidity: int


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    data = resp[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon


def get_weather(lat, lon, API_key):
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}").json()
    weather_data = weather(
        main=data["weather"][0]["main"],
        description=data["weather"][0]["description"],
        icon=data["weather"][0]["icon"],
        temperature=data["main"]["temp"],
        pressure=data["main"]["pressure"],
        humidity=data["main"]["humidity"]
    )
    return weather_data


if __name__ == "__main__":
    lat, lon = get_lat_lon("Kathmandu", NULL, "NP", API_key)
    weather_data = get_weather(lat, lon, API_key)


print(weather_data)
