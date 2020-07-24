from Fichero import *

fichero = Fichero("ficheroBn") #creamos fichero

cadena = "Este es un fichero de prueba donde puedes escribir"
fichero.grabar_fichero(cadena)

cadena2 = "Esta es la segunda que incluyo"
fichero.incluir_fichero(cadena2) #incluimos

fichero.leer_fichero()#leemos fichero