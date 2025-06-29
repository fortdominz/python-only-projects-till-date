# CREATING A TIMES TABLE USING (WHILE LOOP) THAT TAKES INPUT ON THE NUMBER, THE MULTIPLE START, AND THE RANGE

# Now, we prompt the user to give an input for what number times table they want.
num = int(input("What number times table do you want? ")) # Notice the number which starts the times table is changed to 4. i.e: 4 * whatever...
i = int(input("What should the multiple start from? ")) # The start of the times table multiple is also changed, it will start from 1 now; i.e: 4 * 1
length = int(input("What is the length of the times table you want? "))
while i <= length: # The length of the multiple is changed here. This will read from; 4 * 1 till 4 * 20.
    print(f"{num} x {i} = {num * i}")
    i += 1
print(f"{num} times table, completed!\n")


#CREATING A MULTIPLICATION TABLE USING (FOR LOOP) THAT TAKES INPUT FOR BOTH THE NUMBER AND RANGE.
num = int(input("What table multiple do you want? "))
for i in range(int(input("What range are you looking for? "))): # we use range keyword to specify the range of the multiplication.
    print(f"{num} x {i} = {num*i}")
print(f"{num} times table completed!")

# using 99 for the *number input* and 100 for the *range input*, will give you the same result...
#...on both FOR loops

#CREATING A MULTIPLICATION TABLE USING (FOR LOOP)
num = 99
for i in range(100): # we use range keyword to specify the range of the multiplication.
    print(f"{num} x {i} = {num*i}")
print(f"{num} times table completed!")