from tkinter import *
from tkinter import filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
from PIL import ImageFont
from PIL import ImageDraw

FONT = ("Courier", 20, "italic")
FONT_2 = ("Courier", 15, "italic")


window = Tk()
window.title("Add a watermark logo/text")
window.geometry("600x200")
window.config(padx=50, pady=50, bg="#8CB9BD")

label = Label(width=30, text="Choose an image", font=FONT, background="#8CB9BD")
label.grid(column=0, row=0)

button1 = Button(text='Upload File', command=lambda: upload_file())
button1.grid(row=1, column=0)


def upload_file():
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    window.geometry("600x750")
    image = Image.open(filename)
    img1 = image.resize((500, 500))  # new width & height
    img = ImageTk.PhotoImage(img1)
    e1 = Label()
    e1.grid(row=2, column=0)
    e1.image = img  # keep a reference! by attaching it to a widget attribute
    e1['image'] = img  # Show Image

    def text_watermark():
        watermark_image = img1.copy()
        draw = ImageDraw.Draw(watermark_image)

        w, h = img1.size
        x, y = int(w / 2), int(h / 2)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x

        font = ImageFont.truetype("arial.ttf", int(font_size / 6), )

        # get watermark text from user
        watermark_text = askstring('text', 'What is your watermark?')

        # add watermark text to the original picture
        draw.text((120, 480), watermark_text, fill="#747264", font=font, anchor='ms')
        watermark_image.show()

    def logo_watermark():
        # image watermark
        filename1 = filedialog.askopenfilename(filetypes=f_types)
        image2 = Image.open(filename1)
        crop_image = image2.resize((50, 50))  # new width & height

        # add watermark
        copied_image = img1.copy()
        copied_image.paste(crop_image, (100, 430))
        copied_image.show()

    label2 = Label(width=30, text="Choose watermark type", font=FONT_2, background="#8CB9BD")
    label2.grid(column=0, row=3)
    button2 = Button(text='Logo ', command=lambda: logo_watermark())
    button2.grid(row=4, column=0)
    button3 = Button(text='Text ', command=lambda: text_watermark())
    button3.grid(row=5, column=0)


# Run the window's main loop
window.mainloop()
