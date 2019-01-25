class Director:

    def __init__(self):
        self._builder = None

    def constructor(self, builder):
        self._builder = builder
        self._builder._construircabeza()
        self._builder._construirarmadura()
        self._builder._construirarma()
        self._builder._construirpersonaje()
