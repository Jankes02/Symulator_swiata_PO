from Roslina import *


class BarszczSosnowskiego(Roslina):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 10
        self.__sprawdz_sasiadow()

    def umiera(self, zabojca):
        zabojca.usmierc(self)
        self.usmierc(zabojca)

    def __sprawdz_sasiadow(self):
        for kierunek in Kierunek:
            sasiad = self._swiat.sprawdz_pole(self._swiat.get_sasiad(self._pozycja, kierunek))
            if sasiad is not None:
                if self._swiat.czy_zwierze(sasiad):
                    sasiad.usmierc(self)
