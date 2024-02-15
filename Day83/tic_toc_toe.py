from replit import clear

logo = """
   |   |
___|___|___
   |   |
___|___|___
   |   |
   |   |
"""

places = """
 1 | 2 | 3
___|___|___
 4 | 5 | 6
___|___|___
 7 | 8 | 9
   |   |
"""

print(f"Welcome to Tic Tac Toe game.\n{logo}")
player1_char = input("Choose your character. 'X' or 'O'\n").upper()

if player1_char == "X":
    player2_char = "O"
else:
    player2_char = "X"

remained_places = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player1_choices = []
player2_choices = []


def winner():
    global places
    global round_num
    global continue_game
    if round_num >= 3:
        for place in remained_places:
            places = places.replace(place, " ")
        print(places)
        if "1" in player1_choices and "2" in player1_choices and "3" in player1_choices:
            print("Player 1 wins")
        elif "1" in player1_choices and "4" in player1_choices and "7" in player1_choices:
            print("Player 1 wins")
        elif "1" in player1_choices and "5" in player1_choices and "9" in player1_choices:
            print("Player 1 wins")
        elif "3" in player1_choices and "6" in player1_choices and "9" in player1_choices:
            print("Player 1 wins")
        elif "7" in player1_choices and "8" in player1_choices and "9" in player1_choices:
            print("Player 1 wins")
        elif "2" in player1_choices and "5" in player1_choices and "8" in player1_choices:
            print("Player 1 wins")
        elif "4" in player1_choices and "5" in player1_choices and "6" in player1_choices:
            print("Player 1 wins")
        elif "3" in player1_choices and "5" in player1_choices and "7" in player1_choices:
            print("Player 1 wins")
        elif "1" in player2_choices and "2" in player2_choices and "3" in player2_choices:
            print("Player 2 wins")
        elif "1" in player2_choices and "4" in player2_choices and "7" in player2_choices:
            print("Player 2 wins")
        elif "1" in player2_choices and "5" in player2_choices and "9" in player2_choices:
            print("Player 2 wins")
        elif "3" in player2_choices and "6" in player2_choices and "9" in player2_choices:
            print("Player 2 wins")
        elif "7" in player2_choices and "8" in player2_choices and "9" in player2_choices:
            print("Player 2 wins")
        elif "2" in player2_choices and "5" in player2_choices and "8" in player2_choices:
            print("Player 2 wins")
        elif "4" in player2_choices and "5" in player2_choices and "6" in player2_choices:
            print("Player 2 wins")
        elif "3" in player2_choices and "5" in player2_choices and "7" in player2_choices:
            print("Player 2 wins")
        elif round_num > 3:
            print("Tie")


def player(num):
    global places
    clear()
    choice = input(f"{places}\nChoose a place: ")
    if num == 1:
        player1_choices.append(choice)

        # place the choice in the right place of the table
        places = places.replace(choice, player1_char)
        remained_places.remove(choice)

    elif num == 2:
        player2_choices.append(choice)

        # place the choice in the right place of the table
        places = places.replace(choice, player2_char)
        remained_places.remove(choice)


continue_game = True
round_num = 0
while continue_game:
    round_num += 1
    player(1)
    if round_num > 3:
        winner()
        continue_game = False
    else:
        player(2)
