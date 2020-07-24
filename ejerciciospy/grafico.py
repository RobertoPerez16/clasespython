class Person:
    name = ''
    school = ''
    edad=0

    def print_name(self):
        print(self.name)

    def print_school(self):
        print(self.school)

    def EdadDoble(self):
        print("El doble de tu edad es: ",self.edad*2)


jorge = Person()
jorge.name = 'Jorge'
jorge.school = 'Universidad de la vida'
jorge.print_name()
jorge.print_school()

jorge.edad = 22
jorge.EdadDoble()



