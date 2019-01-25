import abc


class Arma():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def imagenarma(self):
        pass
