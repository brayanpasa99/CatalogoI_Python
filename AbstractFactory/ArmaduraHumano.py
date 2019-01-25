import pygame
from AbstractFactory.Armadura import Armadura


class ArmaduraHumano(Armadura):

    def imagenarmadura(self):
        return pygame.transform.scale(pygame.image.load('Imagenes/Armaduras/armadurahumano.png'), (150, 150))
