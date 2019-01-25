import pygame
from AbstractFactory.Personaje import Personaje


class PersonajeHumano(Personaje):

    def imagenpersonaje(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Personajes/personajehumano.png'), (150, 150))
