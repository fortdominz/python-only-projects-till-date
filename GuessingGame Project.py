# GUESSING GAME
import random

guess = 0
randNum = random.randrange(1,11)    #this allows the computer take a number at random, within the range from 1 to 11. This will be the number to be guessed.

while guess != randNum:
    guess = int(input("Try to guess the number: "))
    if guess == randNum:
        print("Correct guess!")
    elif guess > randNum:
        print(f"The number is lesser than {guess}")
    elif guess < randNum:
        print(f"The number is greater than {guess}")

if guess == randNum:
    print("Correct! You guessed right on your first try!")