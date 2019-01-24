import pygame
from pygame.locals import *
import abc
import Armadura
from Armadura import *


class ArmaduraOrco(Armadura):

    def __init__(self):
        pass

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armaduraorco.png'), (150, 150))
