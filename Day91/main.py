from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np


FONT = ("Times New Roman", 30, "bold")
FONT1 = ("Times New Roman", 11)

# Window Setting
window = Tk()
window.title("Image to color list")
window.geometry("600x200")
window.config(padx=50, pady=50, bg="#1B3C73")

# Labels Setting
label = Label(width=3, text="", font=FONT, fg="#FFCAD4", background="#1B3C73")
label.grid(column=0, row=0)
label3 = Label(width=5, text="Choose", font=FONT, fg="#FFCAD4", background="#1B3C73")
label3.grid(column=1,  row=0)
label4 = Label(width=5, text="a", font=FONT, fg="#FFCAD4", background="#1B3C73")
label4.grid(column=2, row=0)
label5 = Label(width=5, text="photo", font=FONT,  fg="#FFCAD4",background="#1B3C73")
label5.grid(column=3, row=0)

# Buttom Setting
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

    # A function that generate hex code based rgb colors
    def rgb_to_hex(r, g, b):
        ans = '{:X}{:X}{:X}'.format(r, g, b)

        while len(ans) < 6:
            ans = "0" + ans

        return "#" + ans

    # A function that find 10 most repeated colors
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
        # Open the phote that user wants
        image = upload_file()
        
        # Turn it to numby array to find its pixle color
        image_array = np.array(image)

        shape = image_array.shape

        x = shape[0]
        y = shape[1]
        
        # Loop through all image pixle and save their rgb colors
        hex_list = []
        for x in range(x):
            for y in range(y):
                rgb = image_array[x, y, :]

                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                hex_list.append(rgb_to_hex(r, g, b))
                
        # Call the defined function to finde most repeated colors 
        top_10_hex = get_top_10(hex_list)

        row = 3
        # New windows setting after uploading image
        window.geometry("600x1000")
        # Create hex code and its color for each color in top 10 colors list
        for color in top_10_hex:
            # Create hex code
            label1 = Label(width=8, text=f"{color}", font=FONT1, fg="white", background="#1B3C73")
            label1.grid(column=1, row=row)
            # Create hex code color
            label2 = Label(width=8, text=" ", background=color)
            label2.grid(column=2, row=row, columnspan=2)
            row += 1
    
    # Show error if user doen't choose an image
    except:
        messagebox.showerror(title="Error", message="No picture Found")

# Run the window's main loop
window.mainloop()
