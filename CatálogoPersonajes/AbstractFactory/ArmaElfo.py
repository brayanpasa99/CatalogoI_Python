import pygame
from pygame.locals import *
import abc
import Arma
from Arma import *


class ArmaElfo(Arma):

    def __init__(self):
        pass

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armaelfo.png'), (150, 150))
