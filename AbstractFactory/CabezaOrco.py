import pygame
from pygame.locals import *
import abc
import Cabeza
from Cabeza import *


class CabezaOrco(Cabeza):

    def __init__(self):
        pass

    def imagencabeza(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Cabezas/cabezaorco.png'), (150, 150))
