import pygame
from AbstractFactory.Arma import Arma


class ArmaElfo(Arma):

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armaelfo.png'), (150, 150))
