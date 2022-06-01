from Organizm import *
from Swiat import *

prawd_rozmnozenia = 15  # %


class Roslina(Organizm):
    _proby_rozmnozenia_na_ture = 1

    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 0
        self._inicjatywa = 0

    def akcja(self):
        for i in range(self._proby_rozmnozenia_na_ture):
            if random.randint(0, 100) < prawd_rozmnozenia:
                self.rozmnoz()
                break

    def rozmnoz(self):
        kierunek = random.randint(0, LICZBA_KIERUNKOW)
        swiat = self._swiat
        sasiad = swiat.sprawdz_pole(swiat.get_sasiad(self._pozycja, Kierunek(kierunek)))
        if sasiad is None:
            swiat.dodaj_organizm(swiat.nowy_organizm(
                            self.to_string(), swiat.get_sasiad(self._pozycja, Kierunek(kierunek))))
