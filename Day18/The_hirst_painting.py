# import colorgram
# colors = colorgram.extract('dot_painting.jpg', 25)
#
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

timmy = Turtle()
my_screen = Screen()
color_list = [(2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 83, 39), (214, 87, 64), (164, 162, 32), (157, 7, 24), (156, 63, 102), (11, 63, 32), (97, 6, 19), (206, 74, 104), (11, 96, 57), (172, 135, 162), (1, 63, 145), (8, 173, 216), (156, 34, 24), (5, 212, 207), (8, 139, 86), (146, 227, 216)]

timmy.penup()
timmy.hideturtle()


x = -225
y = -225
timmy.setposition(x, y)
timmy.speed(0)

for j in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        x += 50
        timmy.setx(x)
    x = -225
    timmy.setx(x)
    y += 50
    timmy.sety(y)

my_screen.exitonclick()

