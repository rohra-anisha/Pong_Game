from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.color("white", color)
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        # self.pendown()
        for i in range(19):
            self.pensize(3)
            self.pendown()
            self.forward(16)
            self.penup()
            self.forward(16)
        self.setheading(0)
        self.goto(x, y)
        self.pendown()
        self.showturtle()
        self.shape(name='square')
        self.turtlesize(stretch_wid=4, stretch_len=1)
#         by default its 20*20

    def up(self):
        self.penup()
        if -245 < self.ycor() < 240:
            self.speed("fastest")
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.penup()
        self.speed("fastest")
        if -240 < self.ycor() < 245:
            self.goto(self.xcor(), self.ycor()-20)

