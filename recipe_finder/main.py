from recipes import *
import os

separator = "_" * 75

def main():
    os.system("clear")
    ingredient = get_user_ingredient()
    category = get_user_category()
    area = get_user_area()
    
    print(f"\n okay, fetching recipes...\n")
    
    recipe_list = search_by_ingredient(ingredient)

    if recipe_list["meals"] == None:
        print(f"\nSorry, i could not find any recipes with that keyword")
        while True:
            try:
                user_retry = True if str(input("Would you like to try again? (y/n)")).lower() == "y" else False
                break
            except:
                print("sorry, i did'nt get that input")
        
        if user_retry == True:
            main()
        else:
            print(f"\nAlright, until next time!")
    
    category_filter = filter_by_category(category, recipe_list)

    area_filter = filter_by_area(area, recipe_list)

    filtered_collection = filtering(recipe_list, category_filter, area_filter)
    
    if filtered_collection != None:
    
        for recipe in filtered_collection:
            print(f"{recipe}\n")
            print("Ingredients:\n")
            for ingredient in filtered_collection[recipe]:
                print(f"{ingredient} - {filtered_collection[recipe][ingredient]}")
            print("\n")
            print(separator)
            
    else:
        print(f"\nSorry, your filters have returned without any appropriate recipes.")
        while True:
            try:
                user_retry = True if str(input("Would you like to try again? (y/n)")).lower() == "y" else False
                break
            except:
                print("sorry, i did'nt get that input")
        
        if user_retry == True:
            main()
        else:
            print(f"\nAlright, until next time!")
        
                

if __name__ == "__main__":
    main()