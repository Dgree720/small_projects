import os
from dotenv import load_dotenv
import requests
from meteostat import Point, Daily, Hourly
from meteostat import Stations



load_dotenv()

weatherapi_key = os.getenv("API_KEY")
geocoding_key = os.getenv("GEOCODING_API_KEY")

base_url = "http://api.weatherapi.com/v1"



class Location:
    
    def __init__(self, location):
        self.location = location
        self.lat, self.lng = self.get_coordinates()
        

    def get_current_weather(self, key = weatherapi_key):
    
        url = f"{base_url}/current.json?key={key}&q={self.location}"
        
        response = requests.get(url)
        
        data = response.json()
        
        return data

    def get_coordinates(self):
    
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.location}&key={geocoding_key}"

        response = requests.get(url)
        
        data = response.json()
        
        lat = round(data["results"][0]["geometry"]["location"]["lat"], ndigits= 4)
        lng = round(data["results"][0]["geometry"]["location"]["lng"], ndigits = 4)
        
        return lat, lng
    
    def fetch_station(self):
        
        stations = Stations()
        stations = stations.nearby(self.lat, self.lng)
        station = stations.fetch(1)

        return station
            
        
    
#lat, lng = get_coordinates("Calw")
#print(f"lat {lat}, lon {lng}")
