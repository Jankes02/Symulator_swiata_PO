import pygame as pg
from Punkt import Punkt
from Kierunek import Kierunek
import random
from Zwierzeta import Antylopa, CyberOwca, Lis, Owca, Wilk, Zolw, Czlowiek
from Rosliny import BarszczSosnowskiego, Guarana, Mlecz, Trawa, WilczeJagody
import os.path

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1200
SURFACE_HEIGHT = 0.7 * SCREEN_HEIGHT
SURFACE_WIDTH = SURFACE_HEIGHT


class Swiat:
    __NAZWY_ORGANIZMOW = ["Czlowiek", "Wilk", "Owca", "Lis", "Antylopa", "Zolw", "CyberOwca", "Mlecz", "Trawa",
                          "Guarana", "WilczeJagody", "BarszczSosnowskiego"]
    __NAZWY_ZWIERZAT = ["Czlowiek", "Wilk", "Owca", "Lis", "Antylopa", "Zolw", "CyberOwca"]
    __ikonki = {}
    __nr_tury = 0
    __kontynuuj = True
    __organizmy = []
    __liczba_organizmow = 0
    __komentarze = []
    __rozmiar_czcionki_komentarzy = 20

    def __init__(self, n, m):
        self.__czlowiek = None
        self.__wysokosc = n
        self.__szerokosc = m
        self.UNIT_SIZE = int(SURFACE_WIDTH / max(m, n))
        pg.init()
        pg.font.init()
        self.__ekran = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.__plansza = pg.Surface((self.__szerokosc * self.UNIT_SIZE, self.__wysokosc * self.UNIT_SIZE)).convert()
        self.__czcionka = pg.font.SysFont("timesnewroman", self.__rozmiar_czcionki_komentarzy)

        for typ in self.__NAZWY_ORGANIZMOW:
            img = pg.image.load(os.path.join("Ikony", typ + ".png"))
            img_scaled = pg.transform.scale(img, (self.UNIT_SIZE, self.UNIT_SIZE))
            self.__ikonki[typ] = img_scaled

    def __ustal_kolejnosc(self):
        self.__organizmy.sort(reverse=True)

    def dodaj_komentarz(self, komentarz):
        self.__komentarze.append(komentarz)

    def kontynuuj(self):
        return self.__kontynuuj

    def get_wysokosc(self):
        return self.__wysokosc

    def get_szerokosc(self):
        return self.__szerokosc

    def get_czlowiek(self):
        return self.__czlowiek

    def get_nr_tury(self):
        return self.__nr_tury

    def __update_info_organizmow(self):
        for org in self.__organizmy:
            org.update_wiek_i_rozmnazanie()

    def __usun_martwe(self):
        for org in self.__organizmy:
            if not org.zyje():
                self.__organizmy.remove(org)
                self.__liczba_organizmow -= 1

    def wykonaj_ture(self, kierunek):
        self.__nr_tury += 1
        self.__update_info_organizmow()
        self.__ustal_kolejnosc()
        last_org = None
        for org in self.__organizmy:
            if org == last_org:
                continue
            org.akcja(kierunek)
            last_org = org

        self.__usun_martwe()
        self.rysuj()

    def rysuj_organizmy(self):
        for org in self.__organizmy:
            if org.zyje():
                self.__plansza.blit(self.__ikonki[org.to_string()],
                                    (org.get_pozycja().x * self.UNIT_SIZE, org.get_pozycja().y * self.UNIT_SIZE))

    def rysuj_plansze(self):
        self.__plansza.fill("#BEBEBE")  # Jasno szary
        for i in range(1, self.__szerokosc):
            pg.draw.line(self.__plansza, (0, 0, 0), (i * self.UNIT_SIZE, 0), (i * self.UNIT_SIZE, SURFACE_HEIGHT))

        for i in range(1, self.__wysokosc):
            pg.draw.line(self.__plansza, (0, 0, 0), (0, i * self.UNIT_SIZE), (SURFACE_WIDTH, i * self.UNIT_SIZE))

    def rysuj_komentarze(self):
        self.__komentarze.insert(0, "Nr tury: " + str(self.__nr_tury))
        pozycja_nastepnego_komentarza = [SURFACE_WIDTH + 10, 0]
        for kom in self.__komentarze:
            do_druku = self.__czcionka.render(kom, False, (0, 0, 0))
            self.__ekran.blit(do_druku, pozycja_nastepnego_komentarza)
            pozycja_nastepnego_komentarza[1] += self.__rozmiar_czcionki_komentarzy + 20

        self.__komentarze.clear()

    def rysuj(self):
        self.__ekran.fill((255, 255, 255))  # Bialy
        self.rysuj_plansze()
        self.rysuj_organizmy()
        self.rysuj_komentarze()
        self.__ekran.blit(self.__plansza, (0, 0))
        pg.display.update()

    def get_sasiad(self, pole, kierunek):
        temp = Punkt(pole.y, pole.x)
        match kierunek:
            case Kierunek.PRAWO:
                if temp.x < self.__szerokosc - 1:
                    temp.x += 1
            case Kierunek.DOL:
                if temp.y < self.__wysokosc - 1:
                    temp.y += 1
            case Kierunek.LEWO:
                if temp.x > 0:
                    temp.x -= 1
            case Kierunek.GORA:
                if temp.y > 0:
                    temp.y -= 1
        return temp

    def nowy_organizm(self, typ_organizmu, pole):
        match typ_organizmu:
            case "Antylopa":
                return Antylopa.Antylopa(pole, self)
            case "Wilk":
                return Wilk.Wilk(pole, self)
            case "Owca":
                return Owca.Owca(pole, self)
            case "Lis":
                return Lis.Lis(pole, self)
            case "Zolw":
                return Zolw.Zolw(pole, self)
            case "CyberOwca":
                return CyberOwca.CyberOwca(pole, self)

            case "Mlecz":
                return Mlecz.Mlecz(pole, self)
            case "Trawa":
                return Trawa.Trawa(pole, self)
            case "Guarana":
                return Guarana.Guarana(pole, self)
            case "WilczeJagody":
                return WilczeJagody.WilczeJagody(pole, self)
            case "BarszczSosnowskiego":
                return BarszczSosnowskiego.BarszczSosnowskiego(pole, self)

            case "Czlowiek":
                return Czlowiek.Czlowiek(pole, self)

    def dodaj_organizm(self, organizm):
        self.__organizmy.insert(0, organizm)
        self.__liczba_organizmow += 1

    def czy_zwierze(self, organizm):
        return organizm.__class__.__name__ in self.__NAZWY_ZWIERZAT

    def sprawdz_pole(self, pole):
        for org in self.__organizmy:
            if org.get_pozycja() == pole:
                return org
        return None

    def nowa_gra(self):
        self.__czlowiek = Czlowiek.Czlowiek(Punkt(self.__wysokosc // 2, self.__szerokosc // 2), self)
        typy = ["Wilk", "Owca", "Lis", "Antylopa", "Zolw", "CyberOwca",
                "Mlecz", "Trawa", "Guarana", "WilczeJagody", "BarszczSosnowskiego"]
        for i in range(2):
            for typ in typy:
                pozycja_dodawanego_organizmu = Punkt(random.randrange(self.__wysokosc),
                                                     random.randrange(self.__szerokosc))
                while self.sprawdz_pole(pozycja_dodawanego_organizmu) is not None \
                        or pozycja_dodawanego_organizmu == self.__czlowiek.get_pozycja():
                    pozycja_dodawanego_organizmu.y = random.randrange(self.__wysokosc)
                    pozycja_dodawanego_organizmu.x = random.randrange(self.__szerokosc)

                self.dodaj_organizm(self.nowy_organizm(typ, pozycja_dodawanego_organizmu))
        self.dodaj_organizm(self.__czlowiek)
        self.rysuj()

    def main_loop(self):
        while self.__kontynuuj:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

                if event.type == pg.KEYDOWN:
                    czlowiek = self.__czlowiek
                    if czlowiek.zyje():
                        if event.key == pg.K_RIGHT:
                            if czlowiek.get_pozycja().x < self.__szerokosc - 1:
                                self.wykonaj_ture(Kierunek.PRAWO)

                        if event.key == pg.K_DOWN:
                            if czlowiek.get_pozycja().y < self.__wysokosc - 1:
                                self.wykonaj_ture(Kierunek.DOL)

                        if event.key == pg.K_LEFT:
                            if czlowiek.get_pozycja().x > 0:
                                self.wykonaj_ture(Kierunek.LEWO)

                        if event.key == pg.K_UP:
                            if czlowiek.get_pozycja().y > 0:
                                self.wykonaj_ture(Kierunek.GORA)

                        if event.key == pg.K_SPACE:
                            if czlowiek.get_special_nr_tury() == 0:
                                czlowiek.set_special_nr_tury(1)
                                czlowiek.set_special_aktywny(True)
                                self.dodaj_komentarz("Aktywacja speciala")
                            elif czlowiek.czy_special_aktywny():
                                self.dodaj_komentarz("Special juz aktywny")
                            else:
                                self.dodaj_komentarz("Jeszcze nie mozesz aktywowac speciala")

                    if event.key == pg.K_k:
                        pg.quit()
                        exit(0)

                    if event.key == pg.K_l:
                        self.wykonaj_ture(None)

                    if event.key == pg.K_p:
                        self.zapisz_gre()
                        pg.quit()
                        exit(0)

    def zapisz_gre(self):
        f = open("saved_game.txt", "w")
        f.write(str(self.__nr_tury) + '\n')
        f.write(str(self.__wysokosc) + " " + str(self.__szerokosc) + '\n')
        f.write(str(self.__liczba_organizmow) + '\n')
        for org in self.__organizmy:
            f.write(org.to_string() + " " + str(org.get_pozycja().y) + " " + str(org.get_pozycja().x) +
                    " " + str(org.get_sila()) + " " + str(org.get_wiek()) + " " + str(self.czy_zwierze(org)))
            if self.czy_zwierze(org):
                f.write(" " + str(org.kiedy_moze_sie_rozmnazac()))
                if org.to_string() == "Czlowiek":
                    f.write(" " + str(org.get_special_nr_tury()) + " " + str(org.czy_special_aktywny()))
            f.write("\n")

        f.write("Nazwa y x sila wiek czy_zwierze (kiedy_rozmnazanie) (special_nr_tury) (special_aktywny)")
        f.close()

    def set_nr_tury(self, nr_tury):
        self.__nr_tury = nr_tury

    @staticmethod
    def wczytaj_gre():
        f = open("saved_game.txt", "r")
        nr_tury = int(f.readline())
        wymiary = f.readline()
        wymiary = wymiary.split(" ")
        wysokosc = int(wymiary[0])
        szerokosc = int(wymiary[1])
        swiat = Swiat(wysokosc, szerokosc)
        liczba_organizmow = int(f.readline())
        swiat.set_nr_tury(nr_tury)
        for i in range(liczba_organizmow):
            line = f.readline()
            line = line.split(" ")
            nazwa_typu = line[0]
            pozycja_organizmu = Punkt(int(line[1]), int(line[2]))
            org = swiat.nowy_organizm(nazwa_typu, pozycja_organizmu)
            sila = int(line[3])
            wiek = int(line[4])
            czy_zwierze = line[5][0] == "T"
            if czy_zwierze:
                tury_przed_rozmnozeniem = int(line[6])
                if nazwa_typu == "Czlowiek":
                    special_nr_tury = int(line[7])
                    special_aktywny = bool(line[8])
                    org.set_special_nr_tury(special_nr_tury)
                    org.set_special_aktywny(special_aktywny)
                    swiat.__czlowiek = org
                else:
                    org.set_tury_przed_rozmnozeniem(tury_przed_rozmnozeniem)
            org.set_sila(sila)
            org.set_wiek(wiek)
            swiat.dodaj_organizm(org)
        f.close()
        return swiat

    def get_organizmy(self):
        return self.__organizmy

    def test(self):
        self.rysuj()
