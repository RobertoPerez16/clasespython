from conectarbd import *

con = Conectar()
#con.crearBD()

#procedemos a insertar los datos
#creamos un menú

while True:
    print("*****Menú de Opciones****")
    print("1. Añadir Producto\n"
          "2. Mostrar Producto\n"
          "3. Salir")
    opc = int(input("Digite su opción: "))
    if opc==1:
        id = input("Digite el id: ")
        nombre = input("Digite el nombre del producto: ")
        precio = input("Digite el precio del producto: ")
        con.InsertarBD(id,nombre,precio)
        print("PRODUCTO AÑADIDO CORRECTAMENTE")

    elif opc==2:
        con.leerDatos()
        con.cerrarconexion()
        print("-------------------")

    elif opc==3:
        print("Adios!!")
        break
