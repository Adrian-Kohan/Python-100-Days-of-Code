from turtle import Turtle
from bullets import Bullet


class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.player_bullet = None
        self.shape("gifs\spaceship.gif")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)
        self.penup()
        self.reposition()

    def reposition(self):
        self.clear()
        self.goto(0,-260)

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def fire(self):
        self.player_bullet = Bullet(self.xcor(), self.ycor(), 90)
        self.player_bullet.bullet_move()


