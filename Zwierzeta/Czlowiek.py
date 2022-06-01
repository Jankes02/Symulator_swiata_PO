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