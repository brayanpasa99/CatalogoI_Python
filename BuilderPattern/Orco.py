from AbstractFactory.FabricaOrcos import FabricaOrcos
from BuilderPattern.Builder import Builder


class Orco(Builder):

    __FabricaOrc = FabricaOrcos()

    def obtenercabeza(self):
        return self.__FabricaOrc.CrearCabeza().imagencabeza()

    def obtenerpersonaje(self):
        return self.__FabricaOrc.CrearPersonaje().imagenpersonaje()

    def obtenerarma(self):
        return self.__FabricaOrc.CrearArma().imagenarma()

    def obtenerarmadura(self):
        return self.__FabricaOrc.CrearArmadura().imagenarmadura()
