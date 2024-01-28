import pandas


alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

continue_asking = True
while continue_asking:
    user_input = input("Enter a word: ")
    try:
        answer = [alphabet_dict[character.upper()] for character in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        continue_asking = False
        print(answer)
