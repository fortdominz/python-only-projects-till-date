# NUMBER GUESSING GAME
import random
from guessinggameart import logo

num = random.randint(1, 100)

not_game_over = True
attempts = 0

def guessing_game():
    """Runs the functionality of the guessing game"""
    print(logo)
    print("Welcome to the Guessing Game 2.0")
    print("I am thinking of a number between 1 and 100\n")
    level = input("Choose your level... easy or hard: \n").lower()

    global not_game_over, attempts

    if level == "easy":
        print("You have 10 attempts. ")
        attempts = 10
    elif level == "hard":
        print("You have 5 attempts. ")
        attempts = 5

    while attempts > 0:
        user_guess = int(input("Guess the number between 1 and 100: \n"))

        if user_guess == num:
            print(f"You guessed correct! The number was {user_guess}")
            not_game_over = False
            break

        attempts -= 1

        if user_guess > num:
            print(f"Your guess {user_guess} is higher than the number")
        elif user_guess < num:
            print(f"Your guess {user_guess} is lower than the number")
        print(f"You have {attempts} attempt(s) left")

    if attempts == 0:
        print(f"Game over! You ran out of guesses. The correct number was: {num}. You lose.")
        not_game_over = False
        return


while not_game_over:
    guessing_game()