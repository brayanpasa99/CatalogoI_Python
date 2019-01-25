import abc
from BuilderPattern.PersonajeCompleto import PersonajeCompleto


class Builder():

    __metaclass__ = abc.ABCMeta

    _PersonajeCompleto = PersonajeCompleto()

    @abc.abstractmethod
    def obtenercabeza(self):
        pass

    @abc.abstractmethod
    def obtenerpersonaje(self):
        pass

    @abc.abstractmethod
    def obtenerarma(self):
        pass

    @abc.abstractmethod
    def obtenerarmadura(self):
        pass
