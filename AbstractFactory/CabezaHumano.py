import pygame
from AbstractFactory.Cabeza import Cabeza


class CabezaHumano(Cabeza):

    def imagencabeza(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Cabezas/cabezahumano.png'), (150, 150))
