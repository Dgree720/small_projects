from retrieve import *
import openai


def extract_weather_data(weather_json):
    
    overview = weather_json["weather"][0]["main"]
        
    return overview

client = openai.OpenAI()

def create_description_prompt(weather_data):
    description_prompt = f"""
    You are a weather description expert.
    You will be supplied with a json formatted data of the current weather at a specific location.
    Create a nice, short and useful description of the weather at the location based on the data.
    
    {weather_data}
    """
    return description_prompt

def create_description(description_prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": description_prompt}],
        temperature=0.2, 
        max_tokens=500, 
    )
    description = response.choices[0].message.content
    return description
    


