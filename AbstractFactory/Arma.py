import abc


class Arma(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def imagenarma(self):
        pass
