from tkinter import *

class Aplicacion:
    def __init__(self):
        self.win = Tk()
        self.win.title("Mi primer App")

        self.etq1 = Label(self.win,text="Nombre: ")
        self.etq1.grid(column=0,row=0)

        self.dato1 = StringVar()
        self.nombre = Entry(self.win, textvariable=self.dato1)
        self.nombre.grid(row=0, column=1)

        self.etq2 = Label(text="Apellido: ")
        self.etq2.grid(row=1,column=0)

        self.dato2 = StringVar()
        self.apellido = Entry(self.win, textvariable=self.dato2)
        self.apellido.grid(row=1,column=1)

        self.button = Button(self.win,text="Mostrar Datos", command=self.MostrarDatos)
        self.button.grid(column=1,row=2)

        self.etqres = Label(text="")
        self.etqres.grid(column=1,row=3)

        self.win.geometry("460x240")
        self.win.mainloop()

    def MostrarDatos(self):
        nom = self.dato1.get()
        ape = self.dato2.get()
        data = nom+" "+ape
        self.etqres.configure(text=data)


aplicacion1=Aplicacion()
