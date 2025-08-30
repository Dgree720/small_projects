import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
key = os.getenv("GMAIL_KEY")
user = os.getenv("MAIL")

def list_messages():
       
    url = f"https://gmail.googleapis.com/gmail/v1/users/{user}/messages"
    
    list = requests.get(url)
    
    return list


print(list_messages())