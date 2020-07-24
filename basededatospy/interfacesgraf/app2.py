from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class App:
    def __init__(self):
        self.win = Tk()
        self.win.title("Mi App")

        #Inicializamos Frame
        self.Frame = Frame(self.win,width=600,height=420)
        self.Frame.config(bg='lightblue')
        self.Frame.pack()

        #Primera Etiqueta y Entry
        Label(self.Frame,text='Nombre:').grid(column=0,row=0)
        self.nombre = Entry(self.Frame)
        self.nombre.grid(column=1,row=0)






        self.win.mainloop()

app = App()