import random

num = random.randint(1, 11)
lives = 3
user_answer = int(input("Guess a number between 1 and 10: "))


while user_answer != num and lives > 1: 
    if user_answer > num:
        print("Too High, guess again")
        lives -= 1  
        user_answer = int(input("Guess a number between 1 and 10: "))
    elif user_answer < num: 
        print("Too Low, guess again")
        lives -= 1
        user_answer = int(input("Guess a number between 1 and 10: "))

if (user_answer == num):
    print(f"Correct! the number is {num}")
else:
    print(f"Incorrect, the number was {num}")

