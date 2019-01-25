import pygame
from AbstractFactory.Armadura import Armadura


class ArmaduraElfo(Armadura):

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armaduraelfo.png'), (150, 150))
