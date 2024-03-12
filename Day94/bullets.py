from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y, head):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.2, stretch_len=0.6)
        self.penup()
        self.goto(x, y)
        self.bullet_speed = 1
        self.setheading(head)

    def bullet_move(self):
        self.forward(self.bullet_speed)

    def detect_lower_limit(self):
        if self.ycor() < - 290:
            self.disappear()

    def detect_top_limit(self):
        if self.ycor() > 290:
            self.disappear()

    def disappear(self):
        self.goto(1000, 1000)
        self.hideturtle()
        self.clear()
        del self


