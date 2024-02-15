from turtle import Turtle
FONT = ("Courier", 60, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.score, align=ALIGNMENT, font=FONT)


    def reset_score(self):
        self.score = 0


    def point(self):
        self.score += 4
        self.update_score()

