from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def game():
    my_screen = Screen()
    my_screen.setup(width=600, height=600)
    my_screen.bgcolor("black")
    my_screen.title("Snake Game")
    my_screen.tracer(0)

    game_is_on = True
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    my_screen.listen()
    my_screen.onkey(snake.move_right, "Right")
    my_screen.onkey(snake.move_down, "Down")
    my_screen.onkey(snake.move_up, "Up")
    my_screen.onkey(snake.move_left, "Left")

    while game_is_on:
        my_screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.score_up()

        # Detect collision with the wall
        if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300
                or snake.segments[0].ycor() < -295):
            game_is_on = False
            scoreboard.game_over()
            answer = my_screen.textinput("Play again", "Do you want to play again? ")
            if answer.lower() == "yes":
                my_screen.clear()
                game()

        # Detect collision with itself
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                answer = my_screen.textinput("Play again", "Do you want to play again? ")
                if answer.lower() == "yes":
                    my_screen.clear()
                    game()


game()
