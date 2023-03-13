import random
import math

num = random.randint(1, 1001)
print(num)
user_answer = int(input("Guess a number between 1 and 1000: "))
no_guesses =  0
algo_guess = 0
binary_search = 500
test_guess = 1000
action = "NA"
possible = list(range(1, 1001))

def find_diff(low, high): #for mid point
    return int((high - low)/2)

while user_answer != num: 
    if user_answer > num:
        print("Too High, guess again")
        user_answer = int(input("Guess a number between 1 and 1000: "))
    elif user_answer < num: 
        print("Too Low, guess again")
        user_answer = int(input("Guess a number between 1 and 1000: "))
    no_guesses += 1

if (user_answer == num):
    print(f"Correct! the number is {num}. It took {no_guesses} guesses")
else:
    print(f"Incorrect, the number was {num}. It took {no_guesses} guesses")

print(f"The max number of guesses is: {int(round(math.log(1000, 2), 0))}") #THIS IS BASICALLY BINARY SEARCH

"""
while (algo_guess < 10):
    if binary_search < test_guess:
        action = "Low"
    elif binary_search > test_guess:
        action = "High"
    if action == "Low":
        for i in possible[0:binary_search]:
            possible.remove(i)
        print(possible)
        print(binary_search)
        print("Guess:", algo_guess)
        binary_search += find_diff(500, 1000)   
    elif action == "High":
        for i in possible[binary_search:len(possible)]:
            possible.remove(i)
        print(possible)
        print(binary_search)
        print("Guess:", algo_guess)
        binary_search -= find_diff(0,500)
    algo_guess += 1
"""       

