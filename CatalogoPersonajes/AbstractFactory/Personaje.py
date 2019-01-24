from abc import ABCMeta, abstractmethod


class Personaje():

    __metaclass__ = ABCMeta

    @abstractmethod
    def imagenpersonaje(self):
        pass
