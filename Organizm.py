LICZBA_KIERUNKOW = 4
from Swiat import *


class Organizm:
    _zabojca = None
    _wiek = 0
    _sila = 0
    _inicjatywa = 0
    _zyje = True

    def __init__(self, pole, swiat):
        self._swiat = swiat
        self._pozycja = pole

    def akcja(self, kierunek_czlowieka=None):
        pass

    def zyje(self):
        return self._zyje

    def umiera(self, zabojca, atakuje=False):
        self.usmierc(zabojca)

    def set_pozycja(self, pole):
        self._pozycja = pole

    def get_pozycja(self):
        return self._pozycja

    def get_zabojca(self):
        return self._zabojca

    def get_sila(self):
        return self._sila

    def get_inicjatywa(self):
        return self._inicjatywa

    def get_wiek(self):
        return self._wiek

    def __gt__(self, drugi):
        if self._inicjatywa > drugi.get_inicjatywa():
            return True

        if self._inicjatywa == drugi.get_inicjatywa():
            return self._wiek > drugi.get_wiek()

        return False

    def to_string(self):
        return self.__class__.__name__

    def update_wiek_i_rozmnazanie(self):
        self._wiek += 1

    def usmierc(self, zabojca):
        self._zabojca = zabojca.to_string() + zabojca.get_pozycja().to_string()
        self._zyje = False
        if self._swiat.czy_zwierze(self):
            self._swiat.dodaj_komentarz(self._zabojca + " zabija " + self.to_string() + self._pozycja.to_string())
        else:
            self._swiat.dodaj_komentarz(self._zabojca + " zjada " + self.to_string() + self._pozycja.to_string())

    def set_sila(self, sila):
        self._sila = sila

    def set_wiek(self, wiek):
        self._wiek = wiek

    def czy_roslina_trujaca(self):
        return self.to_string() == "WilczeJagody" or self.to_string() == "BarszczSosnowskiego"
