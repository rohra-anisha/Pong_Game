from turtle import Turtle
from random import randint
from turtle import Screen
screen = Screen()


class Ball(Turtle):
    def __init__(self, direction):
        # right direction : 1, left direction : -1
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.setheading(45)
        for i in range(25):
            self.clear()
        self.x_move = 5 * direction
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        self.penup()
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -2
        self.move_speed *= 0.9
        # self.y_move *= -2
