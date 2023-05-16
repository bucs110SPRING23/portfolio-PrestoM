import requests
import random

class Meal:
    def __init__(self, ing):
        '''
        Initializes all necessary info to use the meal recipe api (Proxy Class for the MealDB api)
        arg(s): (string) ing - represents the ingrdient the api should use to find a meal with said ingredient
        return: none
        '''
        self.ing = ing
        self.url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={self.ing}"
        self.api = requests.get(self.url)
        self.info = self.api.json()
        try:
            self.meal = self.info["meals"][random.randint(0, len(self.info["meals"])-1)]["strMeal"]
        except:
            self.meal = "None"
        
    def __str__(self):
        return self.api

    def get_meal(self):
        '''
        returns the name of the chosen meal that contains the ingredient stored in self.ing
        arg(s): none
        return: none
        '''
        return self.meal
