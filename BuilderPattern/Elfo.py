from AbstractFactory.FabricaElfos import FabricaElfos
from BuilderPattern.Builder import Builder


class Elfo(Builder):

    __FabricaElf = FabricaElfos()

    def obtenercabeza(self):
        return self.__FabricaElf.CrearCabeza().imagencabeza()

    def obtenerpersonaje(self):
        return self.__FabricaElf.CrearPersonaje().imagenpersonaje()

    def obtenerarma(self):
        return self.__FabricaElf.CrearArma().imagenarma()

    def obtenerarmadura(self):
        return self.__FabricaElf.CrearArmadura().imagenarmadura()
