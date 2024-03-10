from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk
import numpy as np


FONT = ("Times New Roman", 30, "bold")
FONT1 = ("Times New Roman", 11)
FONT2 = ("Times New Roman", 15, "bold")


window = Tk()
window.title("Image to color list")
window.geometry("600x200")
window.config(padx=50, pady=50, bg="#1B3C73")


label = Label(width=3, text="", font=FONT, fg="#FFCAD4", background="#1B3C73")
label.grid(column=0, row=0)
label3 = Label(width=5, text="Choose", font=FONT, fg="#FFCAD4", background="#1B3C73")
label3.grid(column=1,  row=0)
label4 = Label(width=5, text="a", font=FONT, fg="#FFCAD4", background="#1B3C73")
label4.grid(column=2, row=0)
label5 = Label(width=5, text="photo", font=FONT,  fg="#FFCAD4",background="#1B3C73")
label5.grid(column=3, row=0)


button1 = Button(text='Upload File', font=FONT1, command=lambda: run())
button1.grid(row=1, column=1, columnspan=3)


def run():
    def upload_file():
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        window.geometry("600x750")
        image = Image.open(filename)
        img1 = image.resize((400, 400))  # new width & height
        img = ImageTk.PhotoImage(img1)
        e1 = Label()
        e1.grid(row=2, column=1, columnspan=3)
        e1.image = img  # keep a reference! by attaching it to a widget attribute
        e1['image'] = img  # Show Image
        return image

    def rgb_to_hex(r, g, b):
        ans = '{:X}{:X}{:X}'.format(r, g, b)

        while len(ans) < 6:
            ans = "0" + ans

        return "#" + ans

    def get_top_10(hex_list):
        hex_frequency = {}

        for item in hex_list:
            if item in hex_frequency:
                hex_frequency[item] += 1
            else:
                hex_frequency[item] = 1

        sorted_hex = dict(sorted(hex_frequency.items(), key=lambda item: item[1]))

        return list(sorted_hex.keys())[-10:][::-1]

    try:
        image = upload_file()
        image_array = np.array(image)

        shape = image_array.shape

        x = shape[0]
        y = shape[1]

        hex_list = []
        for x in range(x):
            for y in range(y):
                rgb = image_array[x, y, :]

                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                hex_list.append(rgb_to_hex(r, g, b))

        top_10_hex = get_top_10(hex_list)

        row = 3
        window.geometry("600x1000")
        for color in top_10_hex:
            label1 = Label(width=8, text=f"{color}", font=FONT1, fg="white", background="#1B3C73")
            label1.grid(column=1, row=row)
            label2 = Label(width=8, text=" ", background=color)
            label2.grid(column=2, row=row, columnspan=2)
            row += 1

    except:
        messagebox.showerror(title="Error", message="No picture Found")

# Run the window's main loop
window.mainloop()