from re import I
import tkinter as tk
from turtle import bgcolor
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('GUI//files//logo.jpg')
logo = ImageTk.PhotoImage(logo)
logolbl = tk.Label(image=logo, height=100)
logolbl.image = logo
logolbl.grid(column=1, row=0)

infolbl = tk.Label(root, text="Select PDF", fg="#fff", bg="black")
infolbl.grid(columnspan=3, column=0, row=1)

def openFile():
    brwTxt.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF File", "*.pdf")])
    if file:
        print("File opened")
        readPDF = PyPDF2.PdfFileReader(file)
        page = readPDF.getPage(0)
        pageContent = page.extractText()
        print(pageContent)
        
        txtBox = tk.Text(root, height=10, width=50, padx=15, pady=15)
        txtBox.insert(1.0, pageContent)
        txtBox.tag_configure("center", justify="center")
        txtBox.tag_add("center", 1.0, "end")
        txtBox.grid(column=1, row=3)
        
        brwTxt.set("Browse")

brwTxt = tk.StringVar()
brwBtn = tk.Button(root, textvariable=brwTxt, height=2, width=15, fg="white", bg="black", command=lambda:openFile())
brwTxt.set("Browse")
brwBtn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()