from turtle import Turtle
import random

# Class Inheritance: linking attributes from a class to a new class,
# enabling it to have the functionality of the earlier one.
class Food(Turtle): # Turtle here is the superclass

    def __init__(self): # remember: whenever you initialize/create a new object from a class, the init will be called
        super().__init__() # the superclass init: this is like the access card that brings it together
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)