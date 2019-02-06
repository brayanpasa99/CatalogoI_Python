from AbstractFactory.FabricaHumanos import FabricaHumanos
from BuilderPattern.Builder import Builder


class Humano(Builder):

    __FabricaHum = FabricaHumanos()

    def obtenercabeza(self):
        return self.__FabricaHum.CrearCabeza().imagencabeza()

    def obtenerpersonaje(self):
        return self.__FabricaHum.CrearPersonaje().imagenpersonaje()

    def obtenerarma(self):
        return self.__FabricaHum.CrearArma().imagenarma()

    def obtenerarmadura(self):
        return self.__FabricaHum.CrearArmadura().imagenarmadura()
