with open("Input/Letters/starting_letter.txt") as text_file:
    text = text_file.read()

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)

for name in names:
    name_only = name.strip()
    invitation_letter = text.replace("[name]", name_only)
    with open(f"Output/ReadyToSend/letter_for_{name_only}.txt", "w") as invitation:
        invitation.write(invitation_letter)
