# import game_data module, random, art
from higher_lower_game_data import data
import random
from higher_lower_game_art import logo, vs

# The items should show the person's name,
# profession/description and country of origin.
def format_profile(person):
    """Returns a formatted string like: Taylor Swift,
    a Musician, from United States"""

    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}."

# Starts by comparing two items in the data;
# to find which is higher or lower
def compare_followers(person_a, person_b):
    """Returns 'a' if person_a has more followers,
    else 'b' """

    return 'a' if person_a["follower_count"] > person_b["follower_count"] else 'b'

score = 0
game_data = data.copy()
game_over = False

# Picks the next item at random
# Makes sure both items are not the same
a = random.choice(data)
b = random.choice(data)
while b == a:
    b = random.choice(data)

print(logo)
while not game_over:
    print(f"Compare A: {format_profile(a)}")
    print(vs)
    print(f"Against B: {format_profile(b)}\n")

    # Asks user for choice input
    user = input("Who has more instagram followers? Type 'A' or 'B': \n").lower()

    # Clear the screen
    print("\n" * 200)

    # Evaluate the correct answer
    answer = compare_followers(a, b)

    # Compares user answer to the correct answer
    if user == answer:
        # adds 1 point to score, if answer correct
        score += 1
        print(f"Correct! Current score: {score}")
        if answer == "a" or answer == "b":
            # saves previous correct answer to -a-
            a = b
            b = random.choice(data)
            while b == a:
                b = random.choice(data)

        # if correct answer is A or B, a = b, next time
    else:
        print("Sorry, but that is wrong.")
        print(f"Final score is: {score}")
        game_over = True
