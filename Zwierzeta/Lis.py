from Zwierze import *


class Lis(Zwierze):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 3
        self._inicjatywa = 7

    def akcja(self, kierunek_czlowieka=None):
        kierunek = random.randrange(LICZBA_KIERUNKOW)
        for i in range(LICZBA_KIERUNKOW):
            pole = self._swiat.get_sasiad(self._pozycja, kierunek)
            sasiad = self._swiat.sprawdz_pole(pole)
            if sasiad is None or sasiad.get_sila() <= self._sila:
                self.ruch(Kierunek(kierunek))
                break
            kierunek += 1
            kierunek %= LICZBA_KIERUNKOW

        self._sprawdz_barszcz()
