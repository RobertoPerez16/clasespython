from tkinter import *
from tkinter import messagebox
master = Tk()

def addNumbers():
    res = float(e1.get()) + float(e2.get())
    if int(e1.get()) > 3:
        msg = messagebox.showwarning("Atención","el 1 es mayor a 3")
    myText.set(res)

def Resta():
    res = float(e1.get()) - float(e2.get())
    myText.set(res)

def multiplica():
    res = float(e1.get()) * float(e2.get())
    myText.set(res)

myText = StringVar();
Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)
Label(master, text="Result:").grid(row=3)
result = Label(master, text="", textvariable=myText).grid(row=3, column=1)
#La variable stringVar es para pasar un string por parámetro de textvariable

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=0, column=2)
resta = Button(master,text="Resta", command=Resta).grid(row=1,column=2)
mut = Button(master,text="Multiplica", command=multiplica).grid(row=2,column=2)
master.mainloop()



