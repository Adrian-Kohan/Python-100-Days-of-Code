from turtle import Turtle


class Invader(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('gifs\invader.gif')
        self.penup()
        self.speed("slow")
        self.goto(x, y)
        self.setheading(0)
        self.speed = 1

    def move_invader(self):
        self.forward(self.speed)
        self.detect_boundaries()

    def change_direction(self):
        if self.heading() == 0:
            self.setheading(180)
        else:
            self.setheading(0)

    def detect_boundaries(self):
        if self.xcor() > 265 or self.xcor() < -265:
            self.change_direction()

    def delete_invader(self):
        self.goto(3000, 3000)
        self.hideturtle()
        self.clear()
        del self


