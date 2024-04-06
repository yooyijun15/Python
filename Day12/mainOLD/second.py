from art import logo
from random import randint

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Please select'easy' or 'hard'.")    

def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    NUMBER = randint(1,100)
    attempts = choose_difficulty()
    gameStop = False

    while not gameStop and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == NUMBER:
            print(f"You got it😜 The answer was {NUMBER}.")
            gameStop = True
        elif guess > NUMBER:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1

    if not gameStop:
        print(f"You lose😭 The answer was {NUMBER}.")

if input("Do you want to play a game of a Number Guessing Game? Type 'y' or 'n': ") == 'y':
    main()
