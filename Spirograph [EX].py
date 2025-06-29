from turtle import Turtle, Screen
import random
import turtle

neon = Turtle()
neon.shape("turtle")
neon.color("green")

# Making a Spirograph using turtle.
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# for i in range(360):      # this draws a circle
    #     neon.forward(1)
    #     neon.left(1)

def tilt_circle(angle):   # the variable -angle- unit of measurement is degree.
    for _ in range(int(360/angle)):
        neon.color(random_color())
        neon.pensize(2)
        neon.speed("fastest")
        neon.circle(150)
        current_heading = neon.heading()   # turtle's current position in graphical sense; 0.0
        neon.setheading(current_heading + angle)


tilt_circle(5)




screen = Screen()
screen.exitonclick()