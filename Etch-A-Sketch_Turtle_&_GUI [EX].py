from turtle import Turtle, Screen

neon = Turtle()
screen = Screen()

neon.shape("turtle")
neon.color("green")
neon.speed("fastest")

def move_forwards():
    neon.forward(10)

def move_backwards():
    neon.backward(10)

def turn_counter_clockwise():
    neon.left(10)

def turn_clockwise():
    neon.right(10)

def clear():
    neon.reset()
    neon.color("green")


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=neon.reset)
screen.exitonclick()
