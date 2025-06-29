import turtle
from turtle import Turtle
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirstSpotPaintingImg1.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

# All colors have been extracted, hence why the above code is commented.

turtle.colormode(255)

color_list = [(184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48), (57, 137, 121), (108, 40, 29), (22, 65, 50), (40, 80, 7), (94, 62, 68), (110, 8, 9), (199, 91, 65), (116, 167, 77), (131, 178, 92), (224, 231, 225), (139, 167, 175), (216, 202, 142), (178, 147, 150), (179, 205, 177), (225, 177, 167)]
n_of_dots = 100

neon = Turtle()
neon.shape("turtle")
neon.color("green")
neon.speed("fastest")
neon.penup() # to remove the line trails the turtle puts down. the dots will work fine without it
neon.hideturtle()
neon.setheading(225)
neon.forward(300)
neon.setheading(0)


for dots in range(1, n_of_dots + 1):
    neon.dot(20, random.choice(color_list))
    neon.forward(50)

    if dots % 10 == 0:
        neon.setheading(90)
        neon.forward(50)
        neon.setheading(180)
        neon.forward(500)
        neon.setheading(0)



screen = turtle.Screen()
screen.exitonclick()