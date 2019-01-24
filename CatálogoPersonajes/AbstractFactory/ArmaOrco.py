import pygame
from pygame.locals import *
import abc
import Arma
from Arma import *


class ArmaOrco(Arma):

    def __init__(self):
        pass

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armaorco.png'), (150, 150))
