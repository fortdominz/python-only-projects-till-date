print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_bill_w_tip = bill * (1 + tip_percent)
bill_per_person = total_bill_w_tip / people
rounded_bill_per_person = round(bill_per_person, 2)
print(f"Your total bill, including a tip of {tip}% is {total_bill_w_tip}.\nSplitting the bill among {people} persons will equate each person's bill to {rounded_bill_per_person}.")
