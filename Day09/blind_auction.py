from gavel import logo
from replit import clear

print(logo)
print("Welcome to the secret auction program.")
secret_auction = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    secret_auction[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        continue

    elif answer == "no":
        max = 0
        for person in secret_auction:
            if secret_auction[person] > max:
                max = secret_auction[person]
                winner = person
        print(f"The winner is {winner} with a bid of {max}")
        break

