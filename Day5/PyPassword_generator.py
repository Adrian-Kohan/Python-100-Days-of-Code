# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many lettêrs would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for i in range(1, nr_letters + 1):
    index = random.randint(0, len(letters) - 1)
    password += letters[index]
    # or password += random.chioce(letters)

for i in range(1, nr_symbols + 1):
    index = random.randint(0, len(symbols) - 1)
    password += symbols[index]

for i in range(1, nr_numbers + 1):
    index = random.randint(0, len(numbers) - 1)
    password += numbers[index]

# or I could just create a list instead of string for password and shuffle through it (random.shuffle(password))
# to mess up the order and then with a for loop turned it to a string
result = ''.join((random.sample(password, len(password))))
print(f"Yor password is: {result}")
