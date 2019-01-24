import pygame
from pygame.locals import *
import abc
import Armadura
from Armadura import *


class ArmaduraElfo(Armadura):

    def __init__(self):
        pass

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armaduraelfo.png'), (150, 150))
