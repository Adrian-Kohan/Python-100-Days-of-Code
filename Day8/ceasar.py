from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


def caesar(sh, txt, direct):
    # create a new list that holds new encrypted alphabet
    new_alphabet = []
    for i in range(len(alphabet)):
        if (i + shift) < len(alphabet):
            new_alphabet += alphabet[i + shift]
        elif (i + shift) >= len(alphabet) and shift <= len(alphabet):
            start = (i + shift) - len(alphabet)
            new_alphabet += alphabet[start]
        else:
            start = (i + (shift % 26)) - len(alphabet)
            new_alphabet += alphabet[start]

    # decode or encode the text based on the user input
    new_txt = ""
    if direct == "encode":
        for ch in txt:
            if ch in new_alphabet:
                new_txt += new_alphabet[alphabet.index(ch)]
            else:
                new_txt += ch
        print(f"The encoded text is: {new_txt}")

    elif direct == "decode":
        for ch in txt:
            new_txt += alphabet[new_alphabet.index(ch)]
        print(f"The decoded text is: {new_txt}")

# or we can duplicate the alphabet ([a-z,a-z]) and ...
# def caesar(sh, txt, direct):
    # end_txt = ''
    # if direct == "decode":
    #   sh *= -1
    # for letter in txt:
    #   position = alphabet.index(letter)
    #   new_position = position + sh
    #   end_txt += alphabet[new_position]
    # print(f"The {direct}d text is {txt}")


caesar(sh=shift, txt=text, direct=direction)

while True:
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if answer == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(sh=shift, txt=text, direct=direction)
        continue

    elif answer == "no":
        print("Goodbye")
        break


