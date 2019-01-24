from AbstractFactory.ArmaHumano import ArmaHumano
from AbstractFactory.ArmaduraHumano import ArmaduraHumano
from AbstractFactory.CabezaHumano import CabezaHumano
from AbstractFactory.FabricaPrincipal import FabricaPrincipal
from AbstractFactory.PersonajeHumano import PersonajeHumano


class FabricaHumanos(FabricaPrincipal, ArmaduraHumano, ArmaHumano, CabezaHumano, PersonajeHumano):

    def CrearArma(self):
        return ArmaHumano().imagenarma()

    def CrearArmadura(self):
        return ArmaduraHumano().imagenarmadura()

    def CrearCabeza(self):
        return CabezaHumano().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeHumano().imagenpersonaje()
