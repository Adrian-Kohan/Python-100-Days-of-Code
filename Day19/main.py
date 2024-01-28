from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

x = -230
y = -125

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    all_turtle.append(new_turtle)


game_continue = True
if user_bet:
    game_continue = True

while game_continue:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_continue = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

        turtle.forward(random.randint(0, 10))



my_screen.exitonclick()