from turtle import Turtle

FONT = ("Courier", 10, "bold")
FONT1 = ("Courier", 30, "bold")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.high_score = 0
        with open("highest_score.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-290,270)
        self.update_score()

    def update_score(self):
        self.clear()
        score = f"Highest Score: {self.high_score}. Score: {self.score}. lives: {self.lives}"
        self.write(arg=score, align="left", font=FONT, move=False)

    def remove_life(self):
        self.lives -= 1
        self.update_score()

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def result(self, message):
        self.goto(0, 0)
        if message == "Lives":
            self.color("red")
            self.write("Out of lives!\n Game over!", align=ALIGNMENT, font=FONT1, move=False)
        elif message == "Win":
            self.color("yellow")
            self.write("You kill all invaders!\n Well done!", align=ALIGNMENT, font=FONT1, move=False)
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(str(self.high_score))