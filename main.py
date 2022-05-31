from main_menu import *
import pygame as pg
import Swiat

if wymiary_planszy[0] > 0 and wymiary_planszy[1] > 0:
    swiat = Swiat.Swiat(wymiary_planszy[0], wymiary_planszy[1])
    swiat.rysuj()
    while swiat.kontynuuj():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)

            if event.type == pg.K_RIGHT:


elif wymiary_planszy[0] == wymiary_planszy[1] == -1:
    pass
