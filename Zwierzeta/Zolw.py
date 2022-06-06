from Zwierze import *

szansa_na_ruch = 25  # %


class Zolw(Zwierze):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 2
        self._inicjatywa = 1

    def akcja(self, kierunek_czlowieka=None):
        if random.randrange(100) < szansa_na_ruch:
            super().akcja()

    def umiera(self, zabojca, atakuje=False):
        if zabojca.get_sila() > 5:
            self.usmierc(zabojca)
