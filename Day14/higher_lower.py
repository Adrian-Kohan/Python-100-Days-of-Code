from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)


def random_A_and_B():
    """return a random person from list"""
    return random.choice(data)


def logo_display():
    """clear the screen and show the logo"""
    clear()
    print(logo)


def game():
    score = 0
    A = random_A_and_B()
    B = random_A_and_B()
    while True:
        def comparation():
            print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
            print(vs)
            print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

        comparation()
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == 'a':
            if A['follower_count'] > B['follower_count']:
                logo_display()
                score += 1
                print(f"You're right! Current score: {score}")
                A = A
                B = random_A_and_B()
            else:
                logo_display()
                print(f"Sorry, that's wrong. Final score: {score}")
                return
        else:
            if A['follower_count'] < B['follower_count']:
                logo_display()
                score += 1
                print(f"You're right! Current score: {score}")
                A = B
                B = random_A_and_B()
            else:
                logo_display()
                print(f"Sorry, that's wrong. Final score: {score}")
                return

game()
