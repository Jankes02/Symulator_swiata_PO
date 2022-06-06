from Zwierze import *
import math


class CyberOwca(Zwierze):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 11
        self._inicjatywa = 4

    def akcja(self, kierunek_czlowieka=None):
        self.__podazaj_za_barszczem(self.__get_najblizszy_barszcz())

    def __get_najblizszy_barszcz(self):
        swiat = self._swiat
        min_odl = math.sqrt(swiat.get_wysokosc() ** 2 + swiat.get_szerokosc() ** 2)
        barszcz = None

        for org in swiat.get_organizmy():
            if org.to_string() == "BarszczSosnowskiego":
                odl = self._pozycja.odleglosc_do(org.get_pozycja())
                if odl < min_odl:
                    min_odl = odl
                    barszcz = org

        return barszcz

    def __podazaj_za_barszczem(self, barszcz):
        if barszcz is None:
            super().akcja()
        else:
            if self._pozycja.x < barszcz.get_pozycja().x:
                self.ruch(Kierunek.PRAWO)
                return
            if self._pozycja.x > barszcz.get_pozycja().x:
                self.ruch(Kierunek.LEWO)
                return
            if self._pozycja.y < barszcz.get_pozycja().y:
                self.ruch(Kierunek.DOL)
                return
            self.ruch(Kierunek.GORA)

    def usmierc(self, zabojca):
        if zabojca.to_string() != "BarszczSosnowskiego":
            super().usmierc(zabojca)
