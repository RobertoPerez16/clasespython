#diccionarios
"""
diccionario = {
    'nombre':'roberto',
    'apellido':'perez',
    'edad': 20
}

print(diccionario['nombre']," ",diccionario['edad'])
diccionario['estudio'] = 'ing sistemas'
print(diccionario)
"""

"""
#Ejercicio listas

lista = [1,2,5,25,33,56,75,21,56,43,13,62,24]

numabuscar = 21

if numabuscar in lista:
    print(f"El número: {numabuscar} esta en la lista")
else:
    print("el número no se encuentra en la lista")
"""

"""
#Ejercicio bucles

diccionario = {
    'manzana': 'apple',
    'naranja': 'orange',
    'platano': 'banana',
    'limón': 'lemon'
}
print(f"la traducción de la palabra naranja es: {diccionario['naranja']}")

diccionario['piña'] = "pineapple"

for clave,valor in diccionario.items():
    print(clave," : ",valor)
"""

#Ejercicios condicionales

nota = 4.5
trabajo_realizado = 'si'

if(nota >= 4 and trabajo_realizado=='si'):
    nota_final = "Aprobado"
else:
    nota_final = "suspenso..."

print("la nota final es: {}".format(nota_final))


