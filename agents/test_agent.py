from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv
import requests
from meteostat import Point, Daily, Hourly
from meteostat import Stations

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
weatherapi_key = os.getenv("API_KEY")
geocoding_key = os.getenv("GEOCODING_API_KEY")


@tool
def add_numbers(a: int, b: int) -> float:
    """
    Return sum of a and b
    """
    return a + b

@tool
def subtract_numbers(a: int, b: int) -> float:
    """
    Return a minus b
    """
    return a - b

@tool
def divide_numbers(a: int, b: int) -> float:
    """
    Return a divided by b
    """
    return a / b

@tool
def get_weather(city_name, key = weatherapi_key):
    """_summary_

    Args:
        city_name (_type_): the name of the city the user wants to get the weather for
        key (_type_, optional): _description_. Defaults to weather_key.

    Returns:
        _type_: a json formatted description of the weather at the city
    """
    base_url = "http://api.weatherapi.com/v1"

    url = f"{base_url}/current.json?key={key}&q={city_name}"
    
    response = requests.get(url)
    
    data = response.json()
    
    return data



TOOLS = [add_numbers, subtract_numbers, divide_numbers, get_weather]

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    api_key=key  
)
    
    
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a concise, capable assistant. Use tools when they help. "
     "Always explain briefly what you did with a tool before giving the result."
    ),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
    # This placeholder is required so the agent can reason & call tools
    ("placeholder", "{agent_scratchpad}"),
])

# --- 4) Build agent
agent = create_tool_calling_agent(llm, TOOLS, prompt)
executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=False)



def main():
    print("---Agent---")
    chat_history = []
    while True:
        user_input = input("User: ")
    
        result = executor.invoke({
            "input" : user_input,
            "chat_history" : chat_history
        })
        ai_text = result["output"]
        print(f"Agent: {ai_text}")
        
        chat_history.append({"role": "human", "content": user_input})
        chat_history.append({"role": "ai", "content": ai_text})

if __name__ == "__main__":
    main()
    
    
    