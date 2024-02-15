from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os
import PyPDF2


FONT = ("Times New Roman", 30, "bold")


window = Tk()
window.title("Text to Speech")
window.geometry("550x450")
window.config(padx=50, pady=50, bg="#EEEEEE")

label = Label(width=20, text="Upload a pdf file", font=FONT, fg="#3A98B9", background="#EEEEEE")
label.grid(column=0, row=0)

canvas = Canvas(width=400, height=224, bg="#EEEEEE", highlightthickness=0)
img = PhotoImage(file="tts.png")
canvas.create_image(200, 112, image=img)
canvas.grid(column=0, row=1)


button1 = Button(text='Upload File', font=("Times New Roman", 15), width=15, command=lambda: upload_file())
button1.grid(row=2, column=0)


button2 = Button(text='play ', font=("Times New Roman", 15), width=15, command=lambda: play())
button2.grid(row=4, column=0)


def upload_file():
    # opening a pdf file
    f_types = [('pdf file', '*.pdf')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    # creating a pdf file
    pdf = open(filename, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdf)

    # number of pages in pdf file
    num_of_pages = (len(pdfReader.pages))

    # creating a list of pages
    pages = []

    text = ""

    # creating page objects
    for i in range(num_of_pages):
        page = pdfReader.pages[i]
        pages.append(page)

        # extracting text from page
        text += page.extract_text()

    # closing the pdf file
    pdf.close()

    print(text)

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    speech = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file
    speech.save("sound.mp3")


def play():
    # Playing the converted file
    os.system("sound.mp3")


# Run the window's main loop
window.mainloop()
