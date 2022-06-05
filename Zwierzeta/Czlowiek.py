from Zwierze import *


class Czlowiek(Zwierze):
    __special_nr_tury = 0
    __special_aktywny = False

    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)
        self._sila = 5
        self._inicjatywa = 4

    def __sprawdz_speciala(self):
        if self.__special_nr_tury > 0:
            self.__special_nr_tury %= 5
            if self.__special_nr_tury == 0:
                print("Dezaktywacja speciala")
                self.__special_nr_tury -= 5
                self.__special_aktywny = False
            else:
                self.__special_nr_tury += 1
        elif self.__special_nr_tury < 0:
            self.__special_nr_tury += 1

    def akcja(self, kierunek_czlowieka=None):
        if kierunek_czlowieka is not None:
            self.ruch(kierunek_czlowieka)
        self.__sprawdz_speciala()
        self._sprawdz_barszcz()

    def set_special_nr_tury(self, nr_tury):
        self.__special_nr_tury = nr_tury

    def set_special_aktywny(self, czy_aktywny):
        self.__special_aktywny = czy_aktywny

    def get_special_nr_tury(self):
        return self.__special_nr_tury

    def czy_special_aktywny(self):
        return self.__special_aktywny

    def usmierc(self, zabojca):
        self._zyje = False
        # KOMENTARZ?
