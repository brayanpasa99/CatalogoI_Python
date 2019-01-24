import abc
from abc import ABCMeta, abstractmethod


class FabricaPrincipal(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def CrearArma(self):
        pass

    @abstractmethod
    def CrearArmadura(self):
        pass

    @abstractmethod
    def CrearCabeza(self):
        pass

    @abstractmethod
    def CrearPersonaje(self):
        pass
