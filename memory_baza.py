# https://unicode.org/emoji/charts/emoji-list.html#animals_&_nature
from random import shuffle
from statistics import median
import string

lista_emoji = ['\U0001F4A9',
               '\U0001F921',
               '\U0001F47B',
               '\U0001F47D',
               '\U0001F916',
               '\U0001F63A',
               '\U0001F480',
               '\U0001F499'
               ]

lista_znakow = lista_emoji * 2

shuffle(lista_znakow)


def dzielniki(liczba):
    lista_dzielnikow = []
    indeks = 1
    while indeks <= liczba:
        if liczba % indeks == 0:
            lista_dzielnikow.append(indeks)
        indeks += 1
    return lista_dzielnikow


def wymiary_tabeli(dzielniki):
    wymiary = []
    dl = int(len(dzielniki))
    if dl % 2 == 0:
        wymiary.append(dzielniki[int(dl / 2) - 1])
        wymiary.append(dzielniki[int(dl / 2)])
    else:
        wymiary.append(median(dzielniki))
        wymiary.append(median(dzielniki))
    return wymiary


WYMIARY = wymiary_tabeli(dzielniki(len(lista_znakow)))
ILE_RZEDOW = WYMIARY[0]
ILE_KOLUMN = WYMIARY[1]


def stworz_tablice(lista, ilosc_rzedow, ilosc_kolumn):
    ile_znaczkow = len(lista)
    tablica = []
    licznik = 0
    for i in range(ilosc_rzedow):
        licznik = ilosc_kolumn * i
        tablica.append(lista[licznik:(licznik + ilosc_kolumn)])
    return tablica


def wyswietl_tablice(tablica, ilosc_rzedow, ilosc_kolumn):
    print("  ", end=" ")
    for i in string.ascii_letters[26:(26 + ilosc_kolumn - 1)]:
        print(" ", i, end=" ")
    print(" ", string.ascii_letters[26 + ilosc_kolumn - 1])
    for j in range(ilosc_rzedow):
        print(j + 1, " ", end=" ")
        for k in range(ilosc_kolumn):
            print(tablica[j][k], " ", end=" ")
        print()


def nowy_ekran():
    print("\n" * 20)


def obecna_tablica_wyswietl(lista):
    obecna_tablica = stworz_tablice(lista, ILE_RZEDOW, ILE_KOLUMN)
    wyswietl_tablice(obecna_tablica, ILE_RZEDOW, ILE_KOLUMN)
