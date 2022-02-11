from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor)

    def move_up(self):
        new_cor = (self.xcor(), self.ycor() + 20)
        self.goto(new_cor)

    def move_down(self):
        new_cor = (self.xcor(), self.ycor() - 20)
        self.goto(new_cor)
