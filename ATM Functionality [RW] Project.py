# ATM Real-World Functionality
# silly bank by Dominion

import \
    time  # calling the time module  # this imports time commands, so I can make the code wait before taking certain actions
import sys  # this imports system commands

user_balance = 100  # sets user balance
receipt = "No transaction recorded"
transactions = []  # Initialize transaction history list


def about_withdrawal(amount):  # defined a function to carry out repetitive task
    global user_balance, receipt
    user_balance -= amount
    print(f"Successfully withdrawn ${amount}, your new balance is: ${user_balance}")
    receipt = f"You withdrew, ${amount}"
    return receipt


def record_transactions(receipt):
    global transactions
    transactions.append(receipt)
    if len(transactions) > 10:
        transactions.pop(0)  # removes the oldest transaction


def confirm_transaction(message):
    global yes, receipt
    receipt = message
    yes += 1
    record_transactions(receipt)


time.sleep(0.75)
# this makes it so the code waits for 0.75 seconds

print('''
P.S The code is 0192.
Do not use caps.
You can only see your previous 10 transactions.
''')

time.sleep(1)
print('Welcome to silly Banking.')
print()
time.sleep(1)

attempts = True
# creates a variable called "attempts" and sets its value to True

PIN = "0192"

while attempts:  # creates a loop whereas long as attempts is equal to True, the loop will keep going

    attempt1 = (input("Enter your 4-digit PIN: "))
    # creates an input variable named attempt1 that takes only numeric inputs; used to ask for the PIN

    if attempt1 == '0192':  # checks if the input matches the PIN here; 0192
        print("Correct Pin")
        time.sleep(1)
        break
    # If it matches, the user is granted access and the loop breaks

    else:
        print("Incorrect PIN")
        time.sleep(0.75)
        attempt2 = (input("You 2 attempts left. Enter correct PIN: "))
        if attempt2 == '0192':
            print("Correct PIN")
            break

        else:
            print("Incorrect PIN")
            time.sleep(0.75)
            print("You have 1 more attempt")
            attempt3 = (input("Enter correct PIN: "))
            if attempt3 == "0192":
                print("Correct PIN")
                break

            else:
                print("Incorrect PIN")
                # print("Visit any branch near you for help or dail the customer service line to get help remotely")
                print("Wait for 2 minutes to try again. ")
                time.sleep(120)
                # 120 seconds in the timer, makes it so you actually have to wait 2 minutes before it gives you another three attempts
                print()

yes = 0
# creates a variable called "yes" and sets its value to 0

valid_option = True
while valid_option:  # creates another loop
    time.sleep(0.75)
    menu = input('''
    Please select an option:

    Welcome to silly Banking.
    1- Display Balance
    2- Withdraw Funds
    3- Deposit Funds
    4- Print Recent Transactions
    9- Return Card (End Current Session)
    0- Help

    ---->: 
    ''')  # this print the banking menu for the customer to see and select from.
    print()

    # ///////////// DISPLAY BALANCE
    if menu == "1":  # if the customer selects "1", this happens
        print("You have selected '1' - Display Balance")  # says what they selected
        print(f"${user_balance}")
        # instead of printing the start balance of $100, it prints the user's balance by printing the variable that holds the value of the user's balance.
        print()
        time.sleep(0.25)


    # ///////////// WITHDRAW FUNDS
    elif menu == "2":  # if the customer selects "2", this happens
        print("You have selected '2' - Withdraw Funds")  # says what they selected
        time.sleep(0.75)
        try:
            amount = int(input('''
                    How much would you like to withdraw? 

                    Your options are:
                    1
                    5
                    10
                    25
                    50
                    100
                    000 - Other (must be a multiple of 10):
                    123 - Return to main menu
                    999 - Return card (Terminate Current Session)

                    ---->:
                    '''))  # this is the menu option for "2" - Withdraw Funds
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            receipt = "Invalid input: Non-numeric withdrawal attempt"
            record_transactions(receipt)
            continue  # Go back to the menu

        if amount == user_balance:
            user_balance = user_balance - amount
            print(f"You withdrew all funds, your current balance is ${user_balance}")
            # because they withdrew a value equivalent to the user's balance, the user's balance is now 0.
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount > user_balance:
            print("Insufficient balance")
            receipt = "Session ended as there was an insufficient balance"
            yes -= 1
            record_transactions(receipt)

        elif amount == 1:  # used the function I created to output the commented code below
            about_withdrawal(1)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 5:
            about_withdrawal(5)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 10:
            about_withdrawal(10)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 25:
            about_withdrawal(25)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 50:
            about_withdrawal(50)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 100:
            about_withdrawal(100)
            confirm_transaction(f"You withdrew, ${amount}")

        elif amount == 000:
            print("You selected to enter other amount")
            try:
                other_amount = int(input("Enter other amount--- How much would you like to withdraw?: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                receipt = "Invalid input: Non-numeric custom withdrawal amount"
                record_transactions(receipt)
                continue

            # prompts the user to enter an amount
            if other_amount <= 0:
                print("Invalid!")
                print("Withdrawal amount must be greater than 0")
                receipt = f"Transaction failed: Invalid amount!"
                record_transactions(receipt)
            elif other_amount == user_balance:
                print(f"You withdrew all your funds. Successfully withdrew ${user_balance}")
                user_balance -= other_amount
                confirm_transaction(f"You withdrew, ${other_amount}")
            elif other_amount > user_balance:
                print("Insufficient funds")
                receipt = "Session ended as there was an insufficient balance"
                record_transactions(receipt)
            elif other_amount < user_balance and other_amount % 10 == 0:  # the "%" sign calculates for remainder
                # checking if other_amount is a multiple of 10... if equal to 0, then yes, otherwise, no.
                user_balance = user_balance - other_amount
                print(f"Withdrawal processing... ${other_amount}")
                confirm_transaction(f"You withdrew, ${other_amount}")
            else:
                print("Invalid")
                print("Withdrawal amount must be a multiple of 10")
                receipt = "Transaction failed: Amount must be a multiple of 10"
                record_transactions(receipt)


        elif amount == 123:
            print("You selected to go back to main menu")
            print()
            receipt = f"Session cancelled by the user. Returning to the main menu"
            record_transactions(receipt)


        elif amount == 999:
            print(f"Terminating current session... ")
            time.sleep(1)
            print(f"Thank you for banking with us at silly Bank.")
            sys.exit()


        else:
            print("Invalid Option")
            receipt = "Invalid withdrawal option selected"
            record_transactions(receipt)


    # ///////////// DEPOSIT FUNDS
    elif menu == "3":
        print("You have selected to Deposit Funds")
        try:
            options = int(input('''
            Choose an option:

            1- Deposit
            2- Return to main menu
            9- Return card (Cancel current session and head home)

            ---->:
            '''))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            receipt = "Invalid input: Non-numeric deposit menu selection"
            record_transactions(receipt)
            continue

        if options == 1:
            try:
                deposit = int(input("How much would you like to deposit? "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                receipt = "Invalid input: Non-numeric deposit amount"
                record_transactions(receipt)
                continue

            if deposit > 0:
                user_balance += deposit
                print(f"Successfully Deposited, ${deposit}. You now have ${user_balance}")
                confirm_transaction(f"You successfully deposited, ${deposit}")

            elif deposit < 0:
                print("Please input positive number(s)")
                receipt = "Invalid Input. Cannot deposit a negative number"
                record_transactions(receipt)

        elif options == 2:
            print("Returning to main menu")
            receipt = "Transaction session cancelled by the user. Returning to the main menu"
            record_transactions(receipt)

        elif options == 9:
            print("Terminating current session...")
            print("Thank you for banking with us at silly Bank")
            sys.exit()

        else:
            print("Invalid option.")
            receipt = "Invalid deposit menu selection"
            record_transactions(receipt)



    # ////////////// PRINT RECENT TRANSACTIONS
    elif menu == "4":
        print("Transaction History")
        time.sleep(0.75)
        print()
        if transactions:
            for trans in transactions:
                print(trans)
        else:
            print("No transactions recorded yet")


    # ///////////// RETURN CARD
    elif menu == "9":
        print("Terminating Current Session...")
        print("Thank you for banking with us at silly Bank")
        sys.exit()

    elif menu == "0":
        print(
            "Visit our website for additional help or information. If you wish to speak with a live representative, call the help line. Thank you.")

    else:
        print("Please choose a valid option.")
