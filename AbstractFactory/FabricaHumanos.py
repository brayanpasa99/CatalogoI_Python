from AbstractFactory.ArmaHumano import ArmaHumano
from AbstractFactory.ArmaduraHumano import ArmaduraHumano
from AbstractFactory.CabezaHumano import CabezaHumano
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeHumano import PersonajeHumano


class FabricaHumanos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaHumano()

    def CrearArmadura(self):
        return ArmaduraHumano()

    def CrearCabeza(self):
        return CabezaHumano()

    def CrearPersonaje(self):
        return PersonajeHumano()
