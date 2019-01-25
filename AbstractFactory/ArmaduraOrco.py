import pygame
from AbstractFactory.Armadura import Armadura


class ArmaduraOrco(Armadura):

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armaduraorco.png'), (150, 150))
