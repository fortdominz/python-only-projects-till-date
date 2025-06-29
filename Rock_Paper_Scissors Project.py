import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images  = [rock, paper, scissors]

choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper, and 2 for Scissors...\n"))
if choice == 0:
    print(f"Your choice is:\n{choice}")
    print(game_images[choice])
elif choice == 1:
    print(f"Your choice is:\n{choice}")
    print(game_images[choice])
elif choice == 2:
    print(f"Your choice is:\n{choice}")
    print(game_images[choice])
else:
    print("Invalid input: Enter 0 for Rock, 1 for Paper, and 2 for Scissors. ")
    exit()

com = random.randint(0,2)
if com == 0:
    print(f"Computer's choice is:\n{com}")
    print(game_images[com])
elif com == 1:
    print(f"Computer's choice is:\n{com}")
    print(game_images[com])
elif com == 2:
    print(f"Computer's choice is:\n{com}")
    print(game_images[choice])

while True:
    if choice == 0:
        if com == 0:
            print("it is a tie")
        elif com == 1:
            print("Computer wins")
        elif com == 2:
            print("You win")
        else:
            print("Invalid input: Enter 0 for Rock, 1 for Paper, and 2 for Scissors. ")

    elif choice == 1:
        if com == 0:
            print("You win")
        elif com == 0:
            print("It is a tie")
        elif com == 2:
            print("Computer wins")
        else:
            print("Invalid input: Enter 0 for Rock, 1 for Paper, and 2 for Scissors. ")

    elif choice == 2:
        if com == 0:
            print("Computer wins")
        elif com == 1:
            print("You win")
        elif com == 2:
            print("It is a tie")
        else:
            print("Invalid input: Enter 0 for Rock, 1 for Paper, and 2 for Scissors. ")
    else:
        print("Invalid input: Enter 0 for Rock, 1 for Paper, and 2 for Scissors. ")
    break