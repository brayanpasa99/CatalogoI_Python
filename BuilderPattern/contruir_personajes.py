from BuilderPattern.Director import Director
from BuilderPattern.Elfo import Elfo
from BuilderPattern.Humano import Humano


def construir_personajes():
    personajeprueba = Humano()
    director = Director()

    director.cambiarconstructor(personajeprueba)
    personaje = director.obtenerpersonaje()
    personaje.pruebafunciona()

    personajeprueba = Elfo()

    director.cambiarconstructor(personajeprueba)
    personaje = director.obtenerpersonaje()
    personaje.pruebafunciona()

if __name__ == "__main__":
    construir_personajes()
