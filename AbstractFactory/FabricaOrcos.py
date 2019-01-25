from AbstractFactory.ArmaOrco import ArmaOrco
from AbstractFactory.ArmaduraOrco import ArmaduraOrco
from AbstractFactory.CabezaOrco import CabezaOrco
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeOrco import PersonajeOrco


class FabricaOrcos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaOrco()

    def CrearArmadura(self):
        return ArmaduraOrco()

    def CrearCabeza(self):
        return CabezaOrco()

    def CrearPersonaje(self):
        return PersonajeOrco()
