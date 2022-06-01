from main_menu import *
import pygame as pg
import Swiat
import Punkt
import random
random.seed(0)

if wymiary_planszy[0] > 0 and wymiary_planszy[1] > 0:
    swiat = Swiat.Swiat(wymiary_planszy[0], wymiary_planszy[1])
    swiat.rysuj()
    while swiat.kontynuuj():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)

            czlowiek = swiat.get_czlowiek()
            if czlowiek.zyje():
                if event.type == pg.K_RIGHT:
                    if czlowiek.get_pozycja().x < swiat.get_szerokosc() - 1:
                        swiat.wykonaj_ture(Swiat.Kierunek.PRAWO)

                elif event.type == pg.K_DOWN:
                    if czlowiek.get_pozycja().y < swiat.get_wysokosc() - 1:
                        swiat.wykonaj_ture(Swiat.Kierunek.DOL)

                if event.type == pg.K_LEFT:
                    if czlowiek.get_pozycja().x > 0:
                        swiat.wykonaj_ture(Swiat.Kierunek.LEWO)

                elif event.type == pg.K_UP:
                    if czlowiek.get_pozycja().y > 0:
                        swiat.wykonaj_ture(Swiat.Kierunek.GORA)

elif wymiary_planszy[0] == wymiary_planszy[1] == -1:
    pass
