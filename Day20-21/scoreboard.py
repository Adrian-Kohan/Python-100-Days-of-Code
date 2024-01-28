from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.board()

    def board(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.board()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
