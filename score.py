from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def l_scored(self):
        self.l_score += 1

    def r_scored(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.goto(-70, 195)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(70, 195)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
