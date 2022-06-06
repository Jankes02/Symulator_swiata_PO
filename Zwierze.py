from Organizm import *
from Swiat import *

MIN_WIEK_ROZMNAZANIA = 2


class Zwierze(Organizm):
    _tury_przed_nastepnym_rozmnozeniem = 0

    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)

    def ruch(self, kierunek):
        sasiad = self._swiat.sprawdz_pole(self._swiat.get_sasiad(self.get_pozycja(), kierunek))
        if sasiad is None:
            self._pozycja = self._swiat.get_sasiad(self._pozycja, kierunek)
            return True
        elif sasiad is not self:
            self._atakuj(sasiad)
            return True

        return False

    def _atakuj(self, atakowany):
        if self.to_string() == atakowany.to_string():
            atakowany.rozmnoz_sie(self)

        elif self._sila >= atakowany.get_sila() or atakowany.czy_roslina_trujaca():
            pozycja_atakowanego = Punkt(atakowany.get_pozycja().y, atakowany.get_pozycja().x)
            atakowany.umiera(self)
            if not atakowany.zyje() or not atakowany.get_pozycja() == pozycja_atakowanego:
                self._pozycja = pozycja_atakowanego

        else:
            self.umiera(atakowany, True)

    def ucieka(self, atakujacy, atakuje=False):
        kierunek = random.randrange(LICZBA_KIERUNKOW)
        for i in range(LICZBA_KIERUNKOW):
            if atakuje:
                pozycja_sasiada = self._swiat.get_sasiad(atakujacy.get_pozycja(), Kierunek(kierunek))
            else:
                pozycja_sasiada = self._swiat.get_sasiad(self._pozycja, Kierunek(kierunek))
            sasiad = self._swiat.sprawdz_pole(pozycja_sasiada)

            if sasiad is None or sasiad == atakujacy:
                self.set_pozycja(pozycja_sasiada)
                break
            kierunek += 1
            kierunek %= LICZBA_KIERUNKOW

    def update_wiek_i_rozmnazanie(self):
        if self._tury_przed_nastepnym_rozmnozeniem > 0:
            self._tury_przed_nastepnym_rozmnozeniem -= 1
        super().update_wiek_i_rozmnazanie()

    def _sprawdz_barszcz(self):
        for kierunek in Kierunek:
            sasiad = self._swiat.sprawdz_pole(self._swiat.get_sasiad(self._pozycja, kierunek))
            if sasiad is not None:
                if sasiad.to_string() == "BarszczSosnowskiego":
                    self.usmierc(sasiad)
                    break

    def akcja(self, kierunek_czlowieka=None):
        kierunek = random.randrange(LICZBA_KIERUNKOW)
        for i in range(LICZBA_KIERUNKOW):
            if self.ruch(Kierunek(kierunek)):
                break
            kierunek += 1
            kierunek %= LICZBA_KIERUNKOW
        self._sprawdz_barszcz()

    def rozmnoz_sie(self, partner):
        if self._wiek > MIN_WIEK_ROZMNAZANIA and partner.get_wiek() > MIN_WIEK_ROZMNAZANIA \
                and self._tury_przed_nastepnym_rozmnozeniem == 0 and partner.kiedy_moze_sie_rozmnazac() == 0:

            kierunek = random.randrange(LICZBA_KIERUNKOW)
            swiat = self._swiat
            for i in range(LICZBA_KIERUNKOW):
                if swiat.sprawdz_pole(swiat.get_sasiad(self._pozycja, Kierunek(kierunek))) is None:
                    dodany = swiat.nowy_organizm(self.to_string(), swiat.get_sasiad(self._pozycja, Kierunek(kierunek)))
                    swiat.dodaj_organizm(dodany)
                    self._tury_przed_nastepnym_rozmnozeniem = MIN_WIEK_ROZMNAZANIA
                    partner.set_tury_przed_rozmnozeniem(MIN_WIEK_ROZMNAZANIA)
                    self._swiat.dodaj_komentarz(partner.to_string() + partner.get_pozycja().to_string() + " + " +
                                                self.to_string() + self.get_pozycja().to_string() + " = " +
                                                dodany.to_string() + dodany.get_pozycja().to_string())
                    break
                kierunek += 1
                kierunek %= LICZBA_KIERUNKOW

    def kiedy_moze_sie_rozmnazac(self):
        return self._tury_przed_nastepnym_rozmnozeniem

    def set_tury_przed_rozmnozeniem(self, liczba_tur):
        self._tury_przed_nastepnym_rozmnozeniem = liczba_tur
