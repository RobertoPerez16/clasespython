import pickle

fichero = open("fichero.pckl","wb")

frutas = {
    'manzana':'apple',
    'naranja':'orange',
    'plátano':'banana',
    'limón': 'lemon'
}

pickle.dump(frutas,fichero)
fichero.close()

archivo_lec = open("fichero.pckl","rb")
diccionario_a_leer = pickle.load(archivo_lec)

print(diccionario_a_leer)
