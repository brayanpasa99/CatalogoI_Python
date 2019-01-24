from AbstractFactory.ArmaOrco import ArmaOrco
from AbstractFactory.ArmaduraOrco import ArmaduraOrco
from AbstractFactory.CabezaOrco import CabezaOrco
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeOrco import PersonajeOrco


class FabricaOrcos(FabricaPrincipal, ArmaduraOrco, ArmaOrco, CabezaOrco, PersonajeOrco):

    def CrearArma(self):
        return ArmaOrco().imagenarma()

    def CrearArmadura(self):
        return ArmaduraOrco().imagenarmadura()

    def CrearCabeza(self):
        return CabezaOrco().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeOrco().imagenpersonaje()
