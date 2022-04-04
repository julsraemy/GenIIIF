from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

label = Label(text="Let's generate IIIF resources")
label.pack()

var = StringVar()
var.set("IIIF Manifest")
data=("IIIF Manifest", "IIIF Collection")
cb=Combobox(window, values=data)
cb.place(x=20, y=60)

## entry = Entry(width=40, bg="white", fg="black")
## entry.pack()
## entry.insert(0, "What is your name?")

window.mainloop()