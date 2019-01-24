from AbstractFactory.FabricaPrincipal import FabricaPrincipal


class FabricaOrcos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaHumano()

    def CrearArmadura(self):
        return ArmaduraOrco().imagenarmadura()

    def CrearCabeza(self):
        return CabezaOrco().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeOrco().imagenpersonaje()
