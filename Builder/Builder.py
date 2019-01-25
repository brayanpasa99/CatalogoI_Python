import abc


class Builder():

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _construircabeza(self):
        pass

    @abc.abstractmethod
    def _contruirpersonaje(self):
        pass

    @abc.abstractmethod
    def _construirarma(self):
        pass

    @abc.abstractmethod
    def _construirarmadura(self):
        pass
