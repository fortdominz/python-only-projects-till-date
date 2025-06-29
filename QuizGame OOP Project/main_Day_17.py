# Creating a class
# The-class-keyword, followed by the name of your class, and then a colon: and all the code in the class will followed it but indented.
# I.e: class Car:

class User:
    pass

# Working with Attributes, Class Constructors and the __init__() Function -stands for initialization
user_1 = User()
user_1.id = "124218"
user_1.username = "fortdominz"

# print(user_1.username) # output: fortdominz


# Class Constructors ////////////////
class User:
    def __init__(self): # self here specifies the object of the class.
        print("new user being created...")
        # this function will be called everytime you create a new object from this class

user_1 = User() # object here... the variable -user_1-
user_1.id = "124218"
user_1.username = "fortdominz"

print(user_1.username)

user_2 = User() # object here... the variable
user_2.id = "178241"
user_2.username = "xqzboi"

print(user_2.username)
# output:
# new user being created...
# fortdominz
# new user being created...
# xqzboi


# Attributes & Class Constructors /////////////////
class Car:
    def __init__(self, seats): # self here specifies the object of the class. ---- seats is a parameter
        self.seats = seats
        # this function will be called everytime you create a new object from this class

        my_car = Car(5) # 5 represents seats
      # my_car.seats = 5


#   Working on earlier User() class using the __init__() function. /////////////////
class User:
    def __init__(self, user_id, username):
        print("this is first called")
        self.id = user_id
        self.username = username
        self.followers = 0 # This is the default value for all object instanced from this class, notice we didn't put it in the parameter,
                           # therefore it won't be required when you created a new object. When printed, it will give you the default value, 0.

user_1 = User("124218", "fortdominz")
print(user_1.id, user_1.username)
user_2 = User("178241", "xqzboi")
print(user_2.id, user_2.username)


# Attributes & Methods ////////////////////////
# Attributes are the things an object have and methods are the things an object does
# When a function is attached to an object, it's called a method

# Any function defined inside a class is a method

class User:
    def __init__(self, user_id, username):
        print("this is first called")
        self.id = user_id
        self.username = username
        self.followers = 0 # default attribute
        self.following = 0 # default attribute

    def follow(self, user): # self parameter, other user parameter
        user.followers += 1 # user who we are following, their followers goes up by 1
        self.following += 1 # user who followed, their following also goes up by 1


user_1 = User("124218", "fortdominz")
print(user_1.id, user_1.username)
user_2 = User("178241", "xqzboi")
print(user_2.id, user_2.username)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)