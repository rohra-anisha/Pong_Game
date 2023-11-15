from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)
        self.print()

    def increment(self):
        self.score += 1
        self.clear()
        self.print()

    def print(self):
        self.write(f"{self.score}", font=('Courier', 20, 'normal'))
