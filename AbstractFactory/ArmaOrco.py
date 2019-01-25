import pygame
from AbstractFactory.Arma import Arma


class ArmaOrco(Arma):

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armaorco.png'), (150, 150))
