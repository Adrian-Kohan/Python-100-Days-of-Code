from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
new_word = ""
random_word = {}

# ____________________________________Functional Part_________________________________________ #

# check if there is not words to learn to open  then open the French word
try:
    words = pandas.read_csv("data/words_to_learn.csv")
    words_dict = words.to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
    words_dict = words.to_dict(orient="records")


# remove the words that the user knew from the dictionary
def remove_word():
    words_dict.remove(random_word)
    to_learn = pandas.DataFrame(words_dict)
    to_learn.to_csv("data/words_to_learn.csv", index= False)
    random_word_generator()


def flip_cards():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")


def random_word_generator():
    global new_word, random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words_dict)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    flip_timer = window.after(3000, flip_cards)

# ____________________________________User Interface_________________________________________ #


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_sign_img = PhotoImage(file="images/right.png")
wrong_sign_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_sign_img, highlightthickness=0, command=remove_word)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_sign_img, highlightthickness=0, command=random_word_generator)
wrong_button.grid(column=1, row=1)

random_word_generator()
window.mainloop()
