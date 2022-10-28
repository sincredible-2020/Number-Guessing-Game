import random


def game(variable1, variable2):
    if variable1 == "easy":
        count = 10
    else:
        count = 5
    print(f"You have {count} attempts to guess the number.")
    while count != 0:
        guess = int(input("Make a guess: "))
        if guess > variable2:
            print("Too high.")
            count = count - 1
        elif guess < variable2:
            print("Too low.")
            count = count - 1
        else:
            print(f"You got it! The answer was {variable2}")
            break
    if count == 0:
        print("You have run out of guesses. You lose.")


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 101)
game(level, number)
