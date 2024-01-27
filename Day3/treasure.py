print(r'''
      ********************************************
      ********************************************
             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
**************************************************
      ********************************************
      ''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if direction == "left":
    swim_or_boat = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if swim_or_boat == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "yellow":
            print("You win! you found the treasure :)")
        else:
            print("Game Over :(")
    else:
        print("Game Over :(")
else:
    print("Game Over :(")