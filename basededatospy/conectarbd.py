import sqlite3

class Conectar:
    conexion = sqlite3.connect("basededatos.db")

    def crearBD(self):
        cursor = self.conexion.cursor()
        cursor.execute("CREATE TABLE  producto (id INTEGER, nombre TEXT, precio INT)")
        self.conexion.commit()


    def InsertarBD(self, id, nombre, precio):

        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO producto VALUES (?,?,?)",
                           (id,nombre,precio))
        self.conexion.commit()


    def leerDatos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM producto")
        prods = cursor.fetchall()
        for x in range(len(prods)):
            print(prods[x])

        self.conexion.commit()
        self.conexion.close()

    def cerrarconexion(self):
        self.conexion.close()
