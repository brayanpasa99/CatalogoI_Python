import pygame
from AbstractFactory.Personaje import Personaje


class PersonajeElfo(Personaje):

    def imagenpersonaje(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Personajes/personajeelfo.png'), (150, 150))
