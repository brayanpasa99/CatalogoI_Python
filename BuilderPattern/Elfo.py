from BuilderPattern.Builder import Builder


class Elfo(Builder):

    def obtenercabeza(self):
        return "CabezaElfo"

    def obtenerpersonaje(self):
        return "PersonajeElfo"

    def obtenerarma(self):
        return "ArmaHumanoElfo"

    def obtenerarmadura(self):
        return "ArmaduraElfo"
