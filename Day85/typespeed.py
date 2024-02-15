from tkinter import *
import math
import random

sentences = ["Please take your dog, Cali, out for a walk – he really needs some exercise! \n "
             "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
             "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.\n"
             "Do you know why all those chemicals are so hazardous to the environment?",
             "You never did tell me how many copper pennies where in that jar; how come?\n"
             "Max Joykner sneakily drove his car around every corner looking for his dog.",
             "The two boys collected twigs outside, for over an hour, in the freezing cold!\n"
             "When do you think they will get back from their adventure in Cairo, Egypt?",
             "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.\n"
             "We climbed to the top of the mountain in just under two hours; isn’t that great?",
             ]
FONT_NAME = "Courier"
word = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    countdown(60)
    text_input.delete()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    if count_min == 0 and count_sec == "00":
        counter()
# ---------------------------- WORD COUNTER ------------------------------- #


def counter():
    global word
    text = text_input.get()
    word = text.count(" ") + 1

    speed = Label(text=f"Your speed is {word} word per minute", fg="black", bg="#E0CCBE", font=(FONT_NAME, 12, "bold"))
    speed.grid(column=1, row=5)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Typing speed")
window.config(padx=100, pady=50, bg="#E0CCBE")

canvas = Canvas(width=200, height=100, bg="#E0CCBE", highlightthickness=0)
timer_text = canvas.create_text(100, 50, text="00:00", fill="gray", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
start_button = Button(text="Start", bg="#9B4444", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=1, row=2)


# labels

timer_label = Label(text="Timer", fg="#3C3633", bg="#E0CCBE", font=(FONT_NAME, 32, "bold"))
timer_label.grid(column=1, row=0)

sentence = Label(text=random.choice(sentences), fg="black", bg="#E0CCBE", font=(FONT_NAME, 12, "bold"))
sentence.grid(column=1, row=3)

# entries
text_input = Entry(width=200, bd=2)
text_input.grid(column=1, row=4, columnspan=1)
text_input.focus()

window.mainloop()
