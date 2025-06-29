from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.showturtle()

    def move_up(self):
        y = self.ycor()
        if y < 245:
            y += 25
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor()
        if y > -245:
            y -= 25
        self.goto(self.xcor(), y)


