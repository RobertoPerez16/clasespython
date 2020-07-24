#Ejercicios de POO
class Coche:

    def __init__(self, marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrarCaracteristicas(self):
        print("Las características del coche son:\n"
              " marca: ",self.marca,"\n",
              "color: ",self.color,"\n",
              "combustible: ",self.combustible,"\n",
              "cilindrada: ",self.cilindrada)


coche1 = Coche("Audi","Plateado",30,20)

print(coche1.mostrarCaracteristicas())

def calcularProm(nota1,nota2,nota3):
    prom = (nota1+nota2+nota3)/3
    return prom

pr = calcularProm(10,20,30)
print("Promedio de las notas es: ",pr)

