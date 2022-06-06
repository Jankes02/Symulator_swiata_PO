from Roslina import *


class WilczeJagody(Roslina):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 99

    def umiera(self, zabojca, atakuje=False):
        zabojca.usmierc(self)
        self.usmierc(zabojca)
