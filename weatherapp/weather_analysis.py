from retrieve import *



def extract_weather_data(weather_json):
    
    overview = weather_json["weather"]["main"]
    
    return overview

