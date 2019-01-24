import pygame
from pygame.locals import *
import abc
import Personaje
from Personaje import *


class PersonajeHumano(Personaje):

    def __init__(self):
        pass

    def imagenpersonaje(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Personajes/personajehumano.png'), (150, 150))
