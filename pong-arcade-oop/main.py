from turtle import Screen

from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((-375, 0))
paddle2 = Paddle((375, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)
screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    scoreboard.update_scoreboard()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(paddle2) < 50 and ball.xcor() > 340 or ball.distance(paddle1) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detecting when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase_score()

    # Detecting when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_increase_score()


screen.exitonclick()