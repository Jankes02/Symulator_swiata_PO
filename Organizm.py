from Punkt import Punkt
import os.path

LICZBA_KIERUNKOW = 4

class Organizm:
    _zabojca = None
    _wiek = 0
    _sila = 0
    _inicjatywa = 0
    _zyje = True

    def __init__(self, pole, swiat):
        self._swiat = swiat
        self._pozycja = pole
        self._sciezka_ikony = os.path.join("C:\Users\janke\PycharmProjects\PO\ikony", self.__class__.__name__ + ".png")

    def akcja(self):
        pass

    def akcja(self, kierunek_czlowieka):
        self.akcja()

    def zyje(self):
        return self._zyje

    def umiera(self, zabojca):
        self.usmierc(zabojca)

    def get_pozycja(self):
        return self._pozycja

    def get_zabojca(self):
        return self._zabojca

    def get_sila(self):
        return self._sila

    def get_wiek(self):
        return self._wiek

    def get_sciezka_ikony(self):
        return self._sciezka_ikony

    def is_greater(self, drugi):
        if self._inicjatywa > drugi.get_inicjatywa():
            return True

        if self._inicjatywa == drugi.get_inicjatywa():
            return self._wiek > drugi.get_wiek()

        return False

    def to_string(self):
        return self.__class__.__name__

    def usmierc(self, zabojca):
        self._zabojca = zabojca.to_string() + zabojca.get_pozycja().to_string()
        self._zyje = False

    def set_sila(self, sila):
        self._sila = sila

    def set_wiek(self, wiek):
        self._wiek = wiek

    def czy_roslina_trujaca(self):
        return self.to_string() == "WilczeJagody" or self.to_string() == "BarszczSosnowskiego"
