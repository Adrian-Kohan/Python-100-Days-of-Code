import random

word_list = ["ardvark", "baboon", "camel"]
stages =['''
      _______
     |/      |
     |       O
     |
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |       |
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |       |/
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      /
     |
     |___
         ''',
         r'''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / \
     |
     |___
         '''
         ]
lives = 6
#randomly chosen a word from word_list and assign it to a variable named word_chosen
#from hangman_word import word_list
#or import hangman_word
#chosen_word = random.choice(hangman_word.word_list)
chosen_word = random.choice(word_list)
print(r'''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
      ''')

guess_list = []
for i in chosen_word:
    guess_list.append("_")
    #or guess_list += "_"
#ask the user to guess a letter and assign it to a variable called guess. make guess lowercase
s = 0
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #check if the letter user guessed is one of the lettere in the chosen word
    if guess in guess_list:
        print(f"{guess} is already in word.")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guess_list[i] = guess
        print(guess_list)

        if "_" not in guess_list:
            end_of_game = True
            print("You win.")



    elif guess not in chosen_word:
        print(f"{guess} is not in the word so you loose a live")
        lives -= 1
        print(stages[s])
        s += 1
        if lives == 0:
            end_of_game = True
            print(f"{stages[6]}\n You loose.")



