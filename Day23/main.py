from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Passing")
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()
scoreboard = ScoreBoard()

num = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create car every 6 times of the loop
    num += 1
    if num % 6 == 0:
        cars.create_car()
    cars.car_move()

    # detect the level
    if player.next_level():
        scoreboard.level_up()
        cars.speed_up()

    # detect collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
