from AbstractFactory.ArmaElfo import ArmaElfo
from AbstractFactory.ArmaduraElfo import ArmaduraElfo
from AbstractFactory.CabezaElfo import CabezaElfo
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeElfo import PersonajeElfo


class FabricaElfos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaElfo()

    def CrearArmadura(self):
        return ArmaduraElfo()

    def CrearCabeza(self):
        return CabezaElfo()

    def CrearPersonaje(self):
        return PersonajeElfo()
