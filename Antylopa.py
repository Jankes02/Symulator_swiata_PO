from Zwierze import *

szansa_na_ucieczke = 50  # %


class Antylopa(Zwierze):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 4
        self._inicjatywa = 4

    def ruch(self, kierunek):
        swiat = self._swiat
        pole = swiat.get_sasiad(swiat.get_sasiad(self._pozycja, Kierunek(kierunek)), Kierunek(kierunek))
        sasiad = swiat.sprawdz_pole(pole)
        if sasiad is None:
            self._pozycja = pole
            return True

        if sasiad is not self:
            self._atakuj(sasiad)
            return True

        return False

    def umiera(self, zabojca):
        if random.randint(0, 100) < szansa_na_ucieczke:
            self.ucieka(zabojca)
        else:
            self.usmierc(zabojca)
            