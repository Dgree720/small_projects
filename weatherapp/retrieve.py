import requests
import os
import dotenv
import json


dotenv.load_dotenv()
key = os.getenv("API_KEY")

url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={key}"


def get_coordinates_city(city_name = None, state_code = None, country_code = None, key = key):
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={key}"

    response = requests.get(url)
    response = response.json()
    lat = float(round(response[0]["lat"],2))
    lon = float(round(response[0]["lon"],2))
    # print(f"lat -> {lat}, lon -> {lon}")
    return lat, lon



def retrieve_weather_data(lat, lon, key = key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    data = requests.get(url)
    data = data.json()
    print(data)


lat, lon = get_coordinates_city("Stuttgart")
retrieve_weather_data(lat, lon)
