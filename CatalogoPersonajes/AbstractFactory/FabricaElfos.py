from AbstractFactory.ArmaElfo import ArmaElfo
from AbstractFactory.ArmaduraElfo import ArmaduraElfo
from AbstractFactory.CabezaElfo import CabezaElfo
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeElfo import PersonajeElfo


class FabricaElfos(FabricaPrincipal, ArmaduraElfo, ArmaElfo, CabezaElfo, PersonajeElfo):

    def CrearArma(self):
        return ArmaElfo().imagenarma()

    def CrearArmadura(self):
        return ArmaduraElfo().imagenarmadura()

    def CrearCabeza(self):
        return CabezaElfo().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeElfo().imagenpersonaje()
