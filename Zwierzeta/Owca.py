from Zwierze import *


class Owca(Zwierze):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 4
        self._inicjatywa = 4
