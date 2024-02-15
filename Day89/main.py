from tkinter import *


FONT_NAME = "Courier"

timer = None
counter = 0

# ---------------------------- START TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(5)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text,text='00:05')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    canvas.itemconfig(timer_text, text=f"00:0{count}")
    window.config(bg="#B6C4B6")
    canvas.config(bg="#B6C4B6")
    timer_label.config(bg="#B6C4B6")
    sentence.config(bg="#B6C4B6")

    if count == 0:
        reset_timer()
        text_input.delete(0,END)

    if 0 < count < 4:
        window.config(bg="red")
        canvas.config(bg="red")
        timer_label.config(bg="red")
        sentence.config(bg="red", fg="black")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        reset_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_fun():
    global counter
    if counter > 0:
        reset_timer()
    start_timer()
# ---------------------------- DETECT STOP WRITING MECHANISM ------------------------------- #
def stop_writing(event):
    global counter
    counter+=1
    window.after(1000, lambda : timer_fun())

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=100, pady=50, bg="#B6C4B6")

canvas = Canvas(width=200, height=100, bg="#B6C4B6", highlightthickness=0)
timer_text = canvas.create_text(100, 50, text="00:05", fill="gray", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# labels

timer_label = Label(text="Timer", fg="#163020", bg="#B6C4B6", font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

sentence = Label(text="You've only 5 seconds to stop so keep writing!", fg="#EE7214", bg="#B6C4B6", font=(FONT_NAME, 20, "bold"))
sentence.grid(column=1, row=3)

# entries
text_input = Entry(width=200, bd=2)
text_input.grid(column=1, row=4, columnspan=1)
text_input.focus()
text_input.bind('<Key>',lambda event:stop_writing(event))




window.mainloop()
