import pygame
from pygame.locals import *
import abc
import Cabeza
from Cabeza import *


class CabezaElfo(Cabeza):

    def __init__(self):
        pass

    def imagencabeza(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Cabezas/cabezaelfo.png'), (150, 150))
