import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_key = os.getenv("API_key")


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    data = resp[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon


lat, lon = get_lat_lon("New York", "NY", "US", API_key)
print(f"Latitude: {lat}, Longitude: {lon}")
