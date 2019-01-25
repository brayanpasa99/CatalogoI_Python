import pygame
from AbstractFactory.Cabeza import Cabeza


class CabezaOrco(Cabeza):

    def imagencabeza(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Cabezas/cabezaorco.png'), (150, 150))
