from retrieve import *
from weather_analysis import *
import dotenv
import os
import rich

separator = "_" * 75

def main():
    
    
    
    city = get_city_name()
    
    print(f"\n getting weather at location {city}\n")
    print(f"{separator}\n")
    
    lat, lon = get_coordinates_city(city)
    
    weather_json = retrieve_weather_data(lat, lon)
    
    overview = extract_weather_data(weather_json)
    
    description_prompt = create_description_prompt(weather_json)
    
    description = create_description(description_prompt)
    
    print(description)




















if __name__ == "__main__":
    main()