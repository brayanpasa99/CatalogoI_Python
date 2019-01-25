import abc


class FabricaPrincipal():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def CrearArma(self):
        pass

    @abc.abstractmethod
    def CrearArmadura(self):
        pass

    @abc.abstractmethod
    def CrearCabeza(self):
        pass

    @abc.abstractmethod
    def CrearPersonaje(self):
        pass
