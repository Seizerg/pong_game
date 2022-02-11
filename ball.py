from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        new_cor = (self.xcor() + self.x, self.ycor() + self.y)
        self.goto(new_cor)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x *= -1
