import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
weather_key = os.getenv("WEATHER_API_KEY")

def get_city_name():
    while True:
        try:
            city = str(input("What city are you looking for?: ")).capitalize()
            break
        except:
            print("mh, wrong format, please try again with a correct name")
    
    return city

def get_coordinates_city(key = weather_key, city_name = None, state_code = None, country_code = None):
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={key}"

    response = requests.get(url)
    response = response.json()
    print(response)
    lat = float(round(response[0]["lat"],2))
    lon = float(round(response[0]["lon"],2))
    print(f"lat -> {lat}, lon -> {lon}")
    return lat, lon



def retrieve_weather_data(lat, lon, key = weather_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    data = requests.get(url)
    data = data.json()
    print(data)
