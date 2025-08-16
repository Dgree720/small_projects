import requests
from os import getenv
from dotenv import load_dotenv
from json import dumps


BASE_URL = "https://www.themealdb.com/api/json/v1/1/search.php?"


def get_user_ingredient():
    while True:
        try:
            main_ingredient = str(input("Please enter a keyword, or type 'all': ")).lower()
            break
        except:
            print("Invalid entry. Please try again")
    return main_ingredient

def get_user_category():
    while True:
        try:
            category = str(input("please enter a category or type ’all’: ")).capitalize()
            break
        except:
            print("Invalid entry. Please try again")
    return category

def get_user_area():
    while True:
        try:
            area = str(input("please enter an area, or type 'all’: ")).capitalize()
            break
        except:
            print("Invalid entry. Please try again")
    return area
            
    


def search_by_ingredient(ingredient_input):
    
    ingredient = ingredient_input.replace(" ", "_")
    url = f"{BASE_URL}s={ingredient}"
    ingredient_return = requests.get(url)
    ingredient_return.raise_for_status()
    return ingredient_return.json()


def filter_by_category(category, ingredient_return):
    if category == "All":
        category_filter = [recipe["idMeal"] for recipe in ingredient_return["meals"]]
    else:
        category_filter = [recipe["idMeal"] for recipe in ingredient_return["meals"] if recipe["strCategory"] == category]
    return category_filter


def filter_by_area(area, ingredient_return):
        
    if area == "All":
        area_filter = [recipe["idMeal"] for recipe in ingredient_return["meals"]]
    else:
        area_filter = [recipe["idMeal"] for recipe in ingredient_return["meals"] if recipe["strArea"] == area]
    return area_filter


def filtering(ingredient_return, category_filter, area_filter):
    
    if category_filter == [] or area_filter == []:
        combined_filter = set(category_filter) | set(area_filter)
    else:
        combined_filter = set(category_filter) & set(area_filter)
    
    
    filtered_collection = {recipe["strMeal"]:{recipe[f"strIngredient{x}"]:recipe[f"strMeasure{x}"] for x in range(1,21)} for recipe in ingredient_return["meals"] if recipe["idMeal"] in combined_filter}
    
    return filtered_collection


