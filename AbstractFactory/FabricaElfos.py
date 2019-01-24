from AbstractFactory.FabricaPrincipal import FabricaPrincipal


class FabricaElfos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaElfo().imagenarma()

    def CrearArmadura(self):
        return ArmaduraElfo().imagenarmadura()

    def CrearCabeza(self):
        return CabezaElfo().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeElfo().imagenpersonaje()
