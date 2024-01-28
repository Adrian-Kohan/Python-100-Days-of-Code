from turtle import Turtle
FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -320)
        self.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", align= ALIGNMENT, font=FONT)
