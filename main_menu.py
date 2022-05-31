import tkinter as tk
from EntryWithPlaceHolder import *

wymiary_planszy = (-1, -1)


def get_input():
    global wymiary_planszy
    wys = wysokosc_entry.get()
    szer = szerokosc_entry.get()
    if not (wys == "wysokosc" or szer == "szerokosc" or wys == "" or szer == ""):
        wymiary_planszy = (int(wysokosc_entry.get()), int(szerokosc_entry.get()))
        okno_menu.destroy()


def wczyt():
    okno_menu.destroy()


okno_menu = tk.Tk()
okno_menu.geometry('500x500')
okno_menu.title('Menu glowne')
wysokosc_entry = EntryWithPlaceholder(okno_menu, "wysokosc")
wysokosc_entry.pack()
szerokosc_entry = EntryWithPlaceholder(okno_menu, "szerokosc")
szerokosc_entry.pack()
submit = tk.Button(okno_menu, text="Nowa gra", command=get_input)
submit.pack()
wczytaj = tk.Button(okno_menu, text="Wczytaj gre", command=wczyt)
wczytaj.pack()
okno_menu.mainloop()