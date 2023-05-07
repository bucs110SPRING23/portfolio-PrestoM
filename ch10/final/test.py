import requests
import random


#Cocktails

url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
api = requests.get(url)
ing = api.json()["drinks"][0]["strIngredient1"]
#print(ing)

count = 0
keys = api.json()["drinks"][0].keys()
print(keys)

#print (f"strIngredient{random.randint(1,2)}" in keys)
ings = []

#for i in len(api.json()["drinks"][0].keys()):
ing_num = 1
while f"strIngredient{ing_num}" in keys and api.json()["drinks"][0][f"strIngredient{ing_num}"] != None:
    ings.append(f"strIngredient{ing_num}")
    ing_num += 1

print(ings)



#Meals:

url2 = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ing}"
url2 = f"https://www.themealdb.com/api/json/v1/1/filter.php?i=basil"
api2 = requests.get(url2)
meal = api2.json()["meals"][random.randint(0, len(api2.json()["meals"])-1)]["strMeal"]
#print(len(api2.json()["meals"]))
print(f"THE MEAL: {meal}")


"""
url = "https://www.themealdb.com/api/json/v1/1/random.php"
api = requests.get(url)
ing = api.json()["meals"][0]["strIngredient1"]
print(ing)

#Meals:

url2 = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ing}"
api2 = requests.get(url2)
print(api2.json())
"""