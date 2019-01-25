import pygame
from AbstractFactory.Personaje import Personaje


class PersonajeOrco(Personaje):

    def imagenpersonaje(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Personajes/personajeorco.png'), (150, 150))
