from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.penup()
        self.goto(position)

    def disappear(self):
        self.goto(900, 900)