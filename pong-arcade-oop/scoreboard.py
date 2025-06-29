from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=250)
        self.write(self.l_score, align="left", font=("Times New Roman", 30, "italic"))
        self.goto(x=100, y=250)
        self.write(self.r_score, align="right", font=("Times New Roman", 30, "italic"))

    def l_increase_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_increase_score(self):
        self.r_score += 1
        self.update_scoreboard()
