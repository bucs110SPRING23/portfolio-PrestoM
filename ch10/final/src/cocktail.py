import requests
import random

class Cocktail:
    def __init__(self):
        '''
        Initializes all necessary info to use the cocktail recipe api (Proxy Class for the CocktailDB api)
        arg(s): none
        return: none
        '''
        self.api_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
        self.api = requests.get(self.api_url)
        self.gened_cocktails = []
        self.info = self.api.json()
        self.tail_name = self.info["drinks"][0]["strDrink"]
        self.ing = None
        self.ings = []

    def generate_ings(self):
        '''
        generates all the ingredients in a random cocktail and puts the ingredients in the list self.ings
        arg(s): none
        return: none
        '''
        keys = self.info["drinks"][0].keys()
        ing_num = 1
        while (f"strIngredient{ing_num}" in keys) and (self.info["drinks"][0][f"strIngredient{ing_num}"] != None):
            self.ings.append(f"strIngredient{ing_num}")
            ing_num += 1

    def choose_ing(self):
        '''
        chooses a random ingredient from the self.ings list
        arg(s): none
        return: none
        '''
        rand = random.randint(0, len(self.ings)-1)
        ing_num = self.ings[rand]
        self.ing = self.info["drinks"][0][ing_num]

    def get_ing(self):
        '''
        returs the chosen ingredient
        arg(s): none
        return: (string) self.ing - the cocktail ingredient that was chosen randomly
        '''
        return self.ing