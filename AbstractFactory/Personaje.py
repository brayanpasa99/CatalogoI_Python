import abc


class Personaje(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def imagenpersonaje(self):
        pass
