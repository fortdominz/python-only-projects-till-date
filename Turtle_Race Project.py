from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)   # allows programmer to set up the size of screen that will pop up
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "pink"]
y_positions = [-120, -80, -40, 0, 40, 80]
all_turtles = []


def race_positions():
    for turtle_index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-235, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

race_positions()
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You guessed right! The {winner_turtle} turtle won first in the race. ")
            else:
                print(f"You lose! The {winner_turtle} turtle won first in the race. ")
            is_race_on = False
        turtle_speed = random.randint(5, 15)
        turtle.forward(turtle_speed)



screen.exitonclick()