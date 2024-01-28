from tkinter import *

window = Tk()
window.title("Miles o Km Convertor")
window.minsize(200, 100)

label = Label(text="is equal to")
label.grid(column=0, row=1)
label.config(padx=10, pady=10)

label2 = Label(text="0")
label2.grid(column=1, row=1)
label2.config(padx=5, pady=5)


label3 = Label(text="Miles")
label3.grid(column=2, row=0)
label3.config(padx=10, pady=10)


label4 = Label(text="Km")
label4.grid(column=2, row=1)
label4.config(padx=10, pady=10)


user_input = Entry()
user_input.grid(column=1, row=0)


def calculate():
    miles = float(user_input.get()) * 1.609
    label2.config(text=miles)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
