from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

ventana = Tk()
def capturarDatos():
    name = nombre.get()
    ap = apellido.get()
    ed = int(edad.get())
    se = sexo.get()
    message = mb.showinfo("Datos","Nombre: {}\n"
                          "Apellido: {} \n"
                          "Edad: {}\n"
                          "Sexo: {}".format(name,ap,ed,se))


Label(ventana, text="Nombre: ").grid(row=0,column=0)
nombre = Entry(ventana)
nombre.grid(row=0,column=1)

Label(ventana, text="Apellido: ").grid(row=1,column=0)
apellido = Entry(ventana)
apellido.grid(row=1,column=1)

Label(ventana, text="Edad: ").grid(row=2,column=0)
edad = Entry(ventana)
edad.grid(row=2,column=1)

Label(text='Sexo: ').grid(row=3,column=0)

sexo = ttk.Combobox(ventana)
sexo.grid(row=3, column=1)
sexo['values'] = ('Masculino','Femenino','Otro')

boton = Button(text="Mostrar Datos", command=capturarDatos).grid(row=5,column=1)


ventana.title("Programa")
ventana.geometry("300x200")
ventana.mainloop()

