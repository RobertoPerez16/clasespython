from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

#Ventana
ventana = Tk()
ventana.configure(bg='lightblue')
ventana.title("Calculadora")
ventana.resizable(0,0)
#Acciones:

def RealizarCalculos():
    n1= int(numero1.get())
    n2 = int(numero2.get())
    if(op.get() == 'Suma'):
        res = n1+n2
        message = mb.showinfo("Mensaje","La suma de los números es: {}".format(res))

    elif(op.get() == 'Resta'):
        res = n1-n2
        message = mb.showinfo("Mensaje", "La Resta de los números es: {}".format(res))

    elif (op.get() == 'Multiplicación'):
        res = n1*n2
        message = mb.showinfo("Mensaje", "La Multiplicación de los números es: {}".format(res))

    elif (op.get() == 'División'):
        if(n2==0):
            message = mb.showerror("Error","No se puede dividir entre 0")
        else:
            res = n1/n2
            message = mb.showinfo("Mensaje", "La División de los números es: {}".format(res))

    else:
        message = mb.showerror("Error","Operación inválida")


#Componentes

etq1=Label(ventana,text='Digite un número: ')
etq1.grid(row=0,column=0)
etq1.configure(bg='lightblue')
numero1 = StringVar()
num1 = Entry(ventana, textvariable=numero1)
num1.grid(row=0,column=1)

etq2 =Label(ventana,text='Digite otro número: ')
etq2.grid(row=1,column=0)
etq2.configure(bg='lightblue')
numero2 = StringVar()
num2 = Entry(ventana,textvariable=numero2)
num2.grid(row=1,column=1)

etq3 = Label(text='Seleccione: ')
etq3.grid(row=2,column=0)
etq3.configure(bg='lightblue')
op = ttk.Combobox(ventana)
op.grid(row=2,column=1)
op['values'] = ('Suma','Resta','Multiplicación','División')

#Salidas
boton = Button(text='Calcular',bg='lightgray',width=10,command=RealizarCalculos)
boton.grid(row=4,column=1)

botoncerrar = Button(text='Salir',fg='white',bg='red',width=10,command=ventana.quit)
botoncerrar.grid(row=7, column=0)

#ventana
ventana.geometry("340x160")
ventana.mainloop()