from retrieve import *
from weather_analysis import *
import dotenv
import os


def main():
    
    city = get_city_name()
    
    lat, lon = get_coordinates_city(city)
    
    weather_json = retrieve_weather_data(lat, lon)
    
    overview = extract_weather_data(weather_json)
    
    print(overview)




















if __name__ == "__main__":
    main()