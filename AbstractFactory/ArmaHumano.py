import pygame
from pygame.locals import *
import abc
import Arma
from Arma import *


class ArmaHumano(Arma):

    def __init__(self):
        pass

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armahumano.png'), (150, 150))
