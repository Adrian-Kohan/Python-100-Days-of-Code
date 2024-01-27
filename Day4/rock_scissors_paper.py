import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

shapes = [rock, paper, scissors]
user = int(input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer = random.randint(0, 2)

if 0 > user or user >= 3:
    print("You pick up a wrong number so you loose")
else:
    print(shapes[user])
    print("Computer chose:")
    print(shapes[computer])
    if computer == 0 and user == 2:
        print("You lose")
    elif computer == "rock" and user == 0:
        print("It's a draw")
    elif computer == 1 and user == 0:
        print("You lose")
    elif computer == 1 and user == 1:
        print("It's a draw")
    elif computer == 2 and user == 0:
        print("You lose")
    elif computer == 2 and user == 2:
        print("It's a draw")
    else:
        print("You win")
