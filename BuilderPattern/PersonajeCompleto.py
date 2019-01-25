class PersonajeCompleto():

    def __init__(self):
        __cabeza = None
        __arma = None
        __armadura = None
        __personaje = None

    def cambiacabeza(self, cabeza):
        self.__cabeza = cabeza

    def cambiaarma(self, arma):
        self.__arma = arma

    def cambiaarmadura(self, armadura):
        self.__armadura = armadura

    def cambiapersonaje(self, personaje):
        self.__personaje = personaje

    def pruebafunciona(self):
        print self.__arma, self.__armadura, self.__cabeza, self.__personaje



