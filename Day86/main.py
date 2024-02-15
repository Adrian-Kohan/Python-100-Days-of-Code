from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from bricks import Brick
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Breakout Game")
# below method hide the tracer
my_screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
score = Score()

all_bricks = []


# Produce breaks
def breaks():
    global all_bricks
    COLORS = ["red","blue", "green", "yellow", "purple"]
    y = 150
    for color in COLORS:
        x = 380
        for i in range(16):
            pos = (x, y)
            x -= 50
            brick = Brick(pos, color)
            all_bricks.append(brick)
        y -= 25



my_screen.listen()
my_screen.onkey(paddle.move_left, "Left")
my_screen.onkey(paddle.move_right, "Right")

breaks()
game_is_on = True
time_sleep = 0.1
while game_is_on:
    time.sleep(time_sleep)
    # below method show the final tracer
    my_screen.update()
    ball.move()
    # detect collision with the left and right walls
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce_x()
    # detect collision with the left and right walls
    if ball.ycor() > 280:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(paddle) < 50 and ball.ycor() > -250:
        ball.bounce_y()
        time_sleep = 0.1
    # detect paddle misses
    if ball.ycor() < -280:
        breaks()
        score.reset_score()
        score.update_score()
        ball.reset_position()
        time_sleep = 0.1

    # detect collision with bricks
    for brick in all_bricks:
        if  ball.distance(brick) < 40:
            brick.disappear()
            ball.bounce_y()
            score.point()



my_screen.exitonclick()
