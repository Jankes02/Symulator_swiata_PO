#from main_menu import *
import pygame as pg
import Swiat
import random
random.seed()
wymiary_planszy = (10, 10)

if wymiary_planszy[0] > 0 and wymiary_planszy[1] > 0:
    swiat = Swiat.Swiat(wymiary_planszy[0], wymiary_planszy[1])
    swiat.nowa_gra()
    while swiat.kontynuuj():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)

            if event.type == pg.KEYDOWN:
                czlowiek = swiat.get_czlowiek()
                if czlowiek.zyje():
                    if event.key == pg.K_RIGHT:
                        if czlowiek.get_pozycja().x < swiat.get_szerokosc() - 1:
                            swiat.wykonaj_ture(Swiat.Kierunek.PRAWO)

                    if event.key == pg.K_DOWN:
                        if czlowiek.get_pozycja().y < swiat.get_wysokosc() - 1:
                            swiat.wykonaj_ture(Swiat.Kierunek.DOL)

                    if event.key == pg.K_LEFT:
                        if czlowiek.get_pozycja().x > 0:
                            swiat.wykonaj_ture(Swiat.Kierunek.LEWO)

                    if event.key == pg.K_UP:
                        if czlowiek.get_pozycja().y > 0:
                            swiat.wykonaj_ture(Swiat.Kierunek.GORA)

                if event.key == pg.K_k:
                    pg.quit()
                    exit(0)

                if event.key == pg.K_l:
                    swiat.wykonaj_ture(None)

                if event.key == pg.K_p:
                    pass

elif wymiary_planszy[0] == wymiary_planszy[1] == -1:
    pass
