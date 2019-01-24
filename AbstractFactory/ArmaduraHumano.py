import pygame
from pygame.locals import *
import abc
import Armadura
from Armadura import *


class ArmaduraHumano(Armadura):

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armadurahumano.png'), (150, 150))
