class Fichero:
    def __init__(self,nombrefichero):
        self.nombrefichero = nombrefichero

    def leer_fichero(self):
        lec = open(self.nombrefichero,"rt")
        for read in lec.readlines():
            print(read)
        lec.close()

    def grabar_fichero(self,cadena):
        wr = open(self.nombrefichero,"wt")
        wr.write(cadena)
        wr.close()

    def incluir_fichero(self,cadena):
        inc = open(self.nombrefichero,"at")
        inc.write("\n"+cadena)
        inc.close()

