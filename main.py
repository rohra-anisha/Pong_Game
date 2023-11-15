from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title('Pong')
screen.setup(width=800, height=600)
screen.tracer(0)

dir = 1
paddle_r = Paddle(350, 0, "turquoise")
paddle_l = Paddle(-350, 0, "green")
ball = Ball(dir)
score1 = ScoreBoard(50, 240)
score2 = ScoreBoard(-60, 240)

game_on = True
bounce_paddle = False

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.listen()
    screen.onkey(fun=paddle_r.up, key='Up')
    screen.onkey(fun=paddle_r.down, key='Down')
    screen.onkey(fun=paddle_l.up, key='W')
    screen.onkey(fun=paddle_l.down, key='S')
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_wall()

    if ball.distance(paddle_r) <= 20 or (ball.xcor() >= 340 and ball.distance(paddle_r) <= 30 ) or \
            (ball.xcor() <= -330 and ball.distance(paddle_l) <= 40) or ball.distance(paddle_l) <= -20:
        ball.bounce_paddle()
        ball_x = ball.xcor()
        if ball_x > 325:
            score1.increment()
        if ball_x < -325:
            score2.increment()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.hideturtle()
        ball_x = ball.xcor()
        if ball_x > 325:
            score2.increment()
        if ball_x < -325:
            score1.increment()
        dir *= -1
        ball = Ball(dir)
        ball.move_speed = 0.1

screen.exitonclick()
