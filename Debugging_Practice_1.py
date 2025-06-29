# # DESCRIBE THE PROBLEM
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
# my_function()
#
# # Describe the Problem - Write your answers as comments:
# # 1. What is the for loop doing?
# # Iterating through from the set range, 1 - 20
#
# # 2. When is the function meant to print "You got it"?
# # when i equal to  20
#
# # 3. What are your assumptions about the value of i?
# # It never reaches 20, it goes from 1 to 19.
# # Therefore, the print statement never gets executed.
#
#
# # Solution
# def my_function():
#     for i in range(1, 21): # set the end of range, one step higher.
#         if i == 20:
#             print("You got it")
#
# my_function()
#
#
#
# # REPRODUCE THE BUG
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])
#
# # this code will occasionally hit an error when dice_num equal 6.
# # Because 6 is out of index range
# # And dice1 will never get printed as it is in the index 0 which is not given in the randint(range)
#
#
# # Solution
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])
#
#
#
# # PLAY COMPUTER
# year = int(input("What's your year of birth?"))
#
# if 1994 > year > 1980:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
#
# # Here, input 1994 will give nothing, just blank.
# # Because the code give output for if the year is greater than 1994,
# # and for if the year is lesser than 1994
#
#
# # Solution
# year = int(input("What's your year of birth?"))
#
# if 1994 > year > 1980:
#     print("You are a millennial.")
# elif year >= 1994: # Greater than or equal to include 1994 to an output.
#     print("You are a Gen Z.")
#
#
#
# # FIX THE ERRORS
# age = int(input("How old are you?"))
# if age > 18:
#     # print("You can drive at age {age}.")
#
# # So, two things...
# # 1. Indent expected after the if statement to assign the print statement to the if block.
# # 2. f-string... write f in the print statement, but before the opening quotation mark.
#
#
# # Solution
# try: # catching exceptions. Used, so the code doesn't break when input is not an int.
#      # If user enters a str or a value different from an int, it would crash the code and give ValueError message
#     age = int(input("How old are you? \n"))
# except ValueError: # This helps catch it and prints a message you have in mind instead. Maybe instructions, like the one below.
#     print("You have given an invalid input. Please enter a numeric value... e.g 1, 2, 3...")
#     age = int(input("HOw old are you? \n"))
# if age > 18:
#     print(f"You can drive at age {age}.")
#     # print statement indented and f for the f-string added to the print statement.
#
#
#
# # USING PRINT
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # noticed the word_per_page is not being assigned the value of the input,
# # instead, it is comparing 0 (word_per_page start value) to the input by the user.
# # it takes 0 as the value for word_per_page even if an input is given.
# # pages * word_per_page = pages * 0 = 0
#
#
# # Solution
# word_per_page = 0
# print(word_per_page) # added a print statement, so the 0 affects only this section
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#
#
#
# # USING A DEBUGGER
# # USED PYCHARM DEBUGGER FOR THIS ONE
# import random
# import maths
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item) # this is not inside the for block, so it doesn't append all answer values as ecpected, only the last value after the for loop finish running.
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])
# # Output: [single int in the list]
#
#
# # Solution
# import random
# import maths
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item) # this is not inside the for block, so it doesn't append all answer values as ecpected, only the last value after the for loop finish running.
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])
# # output: [multiple int in the list]
#
#
# # TAKE A BREAK
#
#
# # ASK A FRIEND
#
#
# # CHECK IT ONLINE; ASK STACKOVERFLOW
#
#
# # RUN YOUR CODE OFTEN, AS YOU CODE. YOU DO NOT WANT IT TO PILE-UP AND THEN FIND A BUG OR AN ERROR.