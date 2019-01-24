from AbstractFactory.FabricaPrincipal import FabricaPrincipal


class FabricaHumanos(FabricaPrincipal):

    def CrearArma(self):
        return ArmaHumano().imagenarma()

    def CrearArmadura(self):
        return ArmaduraHumano().imagenarmadura()

    def CrearCabeza(self):
        return CabezaHumano().imagencabeza()

    def CrearPersonaje(self):
        return PersonajeHumano().imagenpersonaje()
