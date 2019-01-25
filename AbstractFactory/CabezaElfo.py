import pygame
from AbstractFactory.Cabeza import Cabeza


class CabezaElfo(Cabeza):

    def imagencabeza(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Cabezas/cabezaelfo.png'), (150, 150))
