import pygame
from AbstractFactory.Arma import Arma


class ArmaHumano(Arma):

    def imagenarma(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armas/armahumano.png'), (150, 150))
