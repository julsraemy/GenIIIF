from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

label = Label(text="Let's generate IIIF resources")
label.pack()

# ID (URL) of the IIIF resource

idText=StringVar()
idText.set("What is the URL of the IIIF resource?")
idDir=Label(window, textvariable=idText, height=4)
idDir.pack(side="left")

directory=StringVar(None)
id=Entry(window,textvariable=directory,width=50)
id.insert(0, "https://")
id.pack(side="left")

# Manifest or Collection (context and type)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="IIIF Manifest", variable=v0,value=1)
r2=Radiobutton(window, text="IIIF Collection", variable=v0,value=2)
r1.pack()
r2.pack()

var = StringVar()
var.set("IIIF Manifest")
data=("IIIF Manifest", "IIIF Collection")
cb=Combobox(window, values=data)
cb.place(x=50, y=150)

window.mainloop()