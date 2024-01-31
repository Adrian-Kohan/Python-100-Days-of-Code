from flask import Flask
import random

app = Flask(__name__)
random_num = random.randrange(0, 10)


@app.route('/')
def header():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def checker(number):
    if number == random_num:
        return "<h1>You found me!</h1>"\
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number > random_num:
        return "<h1>Too high, Try again!</h1>"\
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style= 'color: red'>Too low, Try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
