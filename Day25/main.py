import csv
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answer = []

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

while len(correct_answer) < 50:
    answer = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        remained_states = [state for state in states if state not in correct_answer]
        new_data = pandas.DataFrame(remained_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        correct_row = data[data.state == answer]
        state_x = int(correct_row.x)
        state_y = int(correct_row.y)
        correct_state = turtle.Turtle()
        correct_state.hideturtle()
        correct_state.penup()
        correct_state.goto(state_x, state_y)
        correct_state.write(answer)
        correct_answer.append(answer)
