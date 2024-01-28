import random

number_of_attempts = None
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user_choice == "hard":
    print("You have 5 attempts remaining to guess the number.")
    number_of_attempts = 5
elif user_choice == "easy":
    print("You have 10 attempts remaining to guess the number.")
    number_of_attempts = 10


def game(number_of_attempts):
    continue_the_game = True
    remaining_attempts = number_of_attempts
    while continue_the_game:
        guess = int(input("Make a guess: "))
        remaining_attempts -= 1
        if remaining_attempts == 0:
            continue_the_game = False
            print("You've run out of gusses. You lose")
        elif guess > random_number:
            print("Too high")
            print("Guess again.")
            print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        elif guess < random_number:
            print("Too low")
            print("Guess again.")
            print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        else:
            continue_the_game = False
            print(f"You got it! The answer was {random_number}")


game(number_of_attempts)
