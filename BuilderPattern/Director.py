from BuilderPattern.PersonajeCompleto import PersonajeCompleto


class Director():

    _builder = None

    def cambiarconstructor(self, builder):
        self._builder = builder

    def obtenerpersonaje(self):
        personajecompleto = PersonajeCompleto()

        cabeza = self._builder.obtenercabeza()
        personajecompleto.cambiacabeza(cabeza)

        arma = self._builder.obtenerarma()
        personajecompleto.cambiaarma(arma)

        armadura = self._builder.obtenerarmadura()
        personajecompleto.cambiaarmadura(armadura)

        personaje = self._builder.obtenerpersonaje()
        personajecompleto.cambiapersonaje(personaje)

        return personajecompleto

