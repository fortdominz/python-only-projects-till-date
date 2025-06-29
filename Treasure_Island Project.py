print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're in the hallway. There are 2 doors, which do you want to open?\n")
choice1 = input("A or B? ").lower()
print(f"You have selected {choice1}")
if choice1 == "A":
    print("You entered the room where the Lion stays. You were lunch. ")
    print("Game Over!")
elif choice1 == "B":
    print("You went to the ball room. There is a feast among the natives.")
    print("After last night's party, the adventure continues...")
    print("You reach a junction where 2 paths dispel. You are not familiar with where each path leads.")
    print("Which path will you follow despite that?\n")
    choice2 = input("Left or Right? ").lower()
    print(f"You have selected {choice2}")
    if choice2 == "Left":
        print("There was a cliff, you fell off it. There was no survivor.")
        print("Game Over!")
    elif choice2 == "Right":
        print("There was a bridge and a stray horse at the other end of the bridge.")
        print("You take the horse and rode to the next town, nearly 2 hours away.\n"
              "The towns are separated by a lengthy river.")
        print("You see a canoe, but a storm seems to be brewing. "
              "Will you take the canoe and cross just in time, or stay here and wait.")
        choice3 = input("cross or wait? ").lower()
        print(f"You have selected {choice3}")
        if choice3 == "Cross":
            print("It was a heavy storm. You drowned.")
            print("Game Over!")
        elif choice3 == "Wait":
            print("You stand near the river, "
                  "an old couple saw you and invited you into their home because of the incoming rain.\n"
                  "You told them your mission and they present you with the treasure.\n"
                  "They also told you why nobody has ever found the treasure"
                  " is because they were all too eager to cross the river that they all died.\n"
                  "You realize they were ghosts and guardians of the treasure.\nThey disappeared. "
                  "You found the treasure. You won.")
        else:
            print("Not a valid option... Type 'wait' to wait by the river or 'cross' to cross the river.")
    else:
        print("Not a valid option... Type 'left' or 'right' ")
else:
    print("Not a valid option... Type either 'A' or 'B' ")