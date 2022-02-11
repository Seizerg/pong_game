from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Score()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="i", fun=r_paddle.move_up)
screen.onkey(key="k", fun=r_paddle.move_down)

time_speed = 0.1
gameIsOn = True
while gameIsOn:
    time.sleep(time_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 30 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()
        if time_speed > 0:
            time_speed -= 0.01
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_scored()
        score.update_score()
        time_speed = 0.1
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_scored()
        score.update_score()
        time_score = 0.1

screen.exitonclick()
