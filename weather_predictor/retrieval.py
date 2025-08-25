import os
from dotenv import load_dotenv
import requests


load_dotenv()

weatherapi_key = os.getenv("API_KEY")
geocoding_key = os.getenv("GEOCODING_API_KEY")

base_url = "http://api.weatherapi.com/v1"

def get_current_weather(location, key = weatherapi_key):
    
    url = f"{base_url}/current.json?key={key}&q={location}"
    
    response = requests.get(url)
    
    data = response.json()
    
    return data


def get_coordinates(location):
    
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={geocoding_key}"

    response = requests.get(url)
    
    data = response.json()
    
    lat= data["results"][0]["geometry"]["location"]["lat"]
    lng= data["results"][0]["geometry"]["location"]["lng"]
    
    return lat, lng
    

    
#lat, lng = get_coordinates("Calw")
#print(f"lat {lat}, lon {lng}")