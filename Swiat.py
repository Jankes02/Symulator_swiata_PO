import pygame as pg
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SURFACE_HEIGHT = 0.75 * SCREEN_HEIGHT
SURFACE_WIDTH = 0.75 * SCREEN_WIDTH


class Swiat:
    __NAZWY_ZWIERZAT = ["Czlowiek", "Wilk", "Owca", "Lis", "Antylopa", "Zolw"]
    __nr_tury = 0
    __kontynuuj = True
    __organizmy = []
    __liczba_organizmow = 0
    __komentarze = []

    def __init__(self, n, m):
        self.__wysokosc = n
        self.__szerokosc = m
        self.UNIT_SIZE = int(SURFACE_WIDTH / max(m, n))
        pg.init()
        self.__ekran = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.__ekran.fill((255, 255, 255)) #Bialy
        self.__plansza = pg.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
        self.__plansza = self.__plansza.convert()
        self.__plansza.fill("#BEBEBE") #Jasno szary

    def __ustal_kolejnosc(self):
        last_org = None
        for org in self.__organizmy:
            if last_org and org > last_org:
                org, last_org = last_org, org
            else:
                last_org = org

    def kontynuuj(self):
        return self.__kontynuuj

    def get_wysokosc(self):
        return self.__wysokosc

    def get_szerokosc(self):
        return self.__szerokosc

    def __update_info_organizmow(self):
        for org in self.__organizmy:
            org.update_wiek_i_rozmnazanie()

    def __usun_martwe(self):
        for org in self.__organizmy:
            if not org.zyje():
                self.__organizmy.remove(org)

    def wykonaj_ture(self):
        self.__nr_tury += 1
        self.__update_info_organizmow()
        self.__ustal_kolejnosc()
        last_org = None
        for org in self.__organizmy:
            if org == last_org:
                continue
            org.akcja()
            last_org = org

        self.__usun_martwe()
        self.rysuj()

    def rysuj(self):
        pg.draw.rect(self.__plansza, (100, 0, 0), pg.Rect((0, 0), (SURFACE_WIDTH, SURFACE_HEIGHT)))
        self.__ekran.blit(self.__plansza, (0, 0))
        pg.display.update()

    def test(self):
        self.rysuj()
