import abc


class Personaje():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def imagenpersonaje(self):
        pass
