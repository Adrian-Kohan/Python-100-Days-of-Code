from turtle import Screen
from paddles import Paddle
from ball import Ball
from middleline import MidLine
from score import Score
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
# below method hide the tracer
my_screen.tracer(0)

right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))
ball = Ball()
midline = MidLine()
score = Score()

my_screen.listen()
my_screen.onkey(right_paddle.move_up, "Up")
my_screen.onkey(right_paddle.move_down, "Down")
my_screen.onkey(left_paddle.move_up, "w")
my_screen.onkey(left_paddle.move_down, "s")

game_is_on = True
time_sleep = 0.1
while game_is_on:
    time.sleep(time_sleep)
    # below method show the final tracer
    my_screen.update()
    ball.move()
    # detect collision with the top and down walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time_sleep *= 0.7
    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        time_sleep = 0.1
        score.l_point()
    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        time_sleep = 0.1
        score.r_point()

my_screen.exitonclick()
