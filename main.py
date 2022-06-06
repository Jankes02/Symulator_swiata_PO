from main_menu import *
import Swiat
import random
random.seed()

if wymiary_planszy[0] > 0 and wymiary_planszy[1] > 0:
    swiat = Swiat.Swiat(wymiary_planszy[0], wymiary_planszy[1])
    swiat.nowa_gra()
    swiat.main_loop()

elif wymiary_planszy[0] == wymiary_planszy[1] == -1:
    swiat = Swiat.Swiat.wczytaj_gre()
    swiat.rysuj()
    swiat.main_loop()
