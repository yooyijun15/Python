from art import logo
import random

if input("Do you want to play a game of a Number Guessing Game? Type 'y' or 'n': ") == 'y':
    NUMBER = random.randint(1,100)
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Select'easy' or 'hard'")
    gameStop = False
    while not gameStop and attempts!=0:
        answer = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
        if answer == NUMBER:
            print(f"You got it😜 The answer was {NUMBER}.")
            gameStop = True
        elif answer > NUMBER:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
    if attempts == 0 and gameStop == False:
        print(f"You lose😭 The answer was {NUMBER}.")
