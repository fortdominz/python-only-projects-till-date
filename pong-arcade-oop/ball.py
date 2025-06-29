from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_pace = 10
        self.y_pace = 10
        self.ball_speed = 0.075

    def move(self):
        x = self.xcor()
        x += self.x_pace
        y = self.ycor()
        y += self.y_pace
        self.goto(x, y)

    def bounce_y(self):
        self.y_pace *= -1
        self.ball_speed *= 0.9


    def bounce_x(self):
        self.x_pace *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.075
        self.bounce_x()

