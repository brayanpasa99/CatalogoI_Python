from BuilderPattern.Builder import Builder


class Humano(Builder):

    def obtenercabeza(self):
        return "CabezaHumano"

    def obtenerpersonaje(self):
        return "PersonajeHumano"

    def obtenerarma(self):
        return "ArmaHumano"

    def obtenerarmadura(self):
        return "ArmaduraHumano"
