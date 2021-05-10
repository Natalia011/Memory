import memory_baza as baza


def wybierz_symbol(znak):
    znak = list(znak)
    try:
        r = znak[0].upper()
        c = znak[1]
        id_znak = ord(r) - 65 + baza.ILE_RZEDOW * (int(c) - 1)
        symbol = baza.lista_znakow[id_znak]
        wynik = [id_znak, symbol]
        if obecna_lista[wynik[0]] != '*':
            raise ValueError
        else:
            obecna_lista[wynik[0]] = wynik[1]
        return wynik
    except (IndexError, ValueError):
        print('Błędne koordynaty lub ten symbol jest już odkryty!\n')
        pass


def podaj_koordynaty(wynik=None, licznik_wywolan=0):
    while wynik == None:
        if licznik_wywolan == 0:
            znak = input('Którą \'gwiazdkę\' mam odkryć jako pierwszą? (np.A1): ')
        else:
            znak = input('Podaj drugą \'gwiazdkę\': ')
        wynik = wybierz_symbol(znak)
    return wynik


# ROZGRYWKA:
licznik_prob = 10
print(f'Masz {licznik_prob} prób(y). Powodzenia! :)')
obecna_lista = ['*'] * baza.ILE_RZEDOW * baza.ILE_KOLUMN

while licznik_prob > 0:
    baza.obecna_tablica_wyswietl(obecna_lista)

    wynik1 = podaj_koordynaty()
    baza.obecna_tablica_wyswietl(obecna_lista)
    wynik2 = podaj_koordynaty(licznik_wywolan=1)

    if wynik1[0] == wynik2[0]:
        print('Podałeś te same koordynaty! Graj dalej.')
        print(f'Pozostałe próby: {licznik_prob}\n')
        obecna_lista[wynik1[0]] = '*'
        continue

    if wynik1[1] == wynik2[1]:
        if '*' not in obecna_lista:
            print('#' * 20, 'GRATULUJĘ WYGRANEJ!!!', '#' * 20)
            print('Twoja tablica:')
            baza.obecna_tablica_wyswietl(obecna_lista)
            exit()
        else:
            print('Brawo! Zgaduj dalej :)')
    else:
        licznik_prob -= 1
        baza.obecna_tablica_wyswietl(obecna_lista)
        print('\nNiestety, niepoprawnie. Zapamiętaj ułożenie symboli.')
        reakcja = input('Naciśnij ENTER jeśli mogę przejść dalej.')
        baza.nowy_ekran()
        obecna_lista[wynik1[0]] = '*'
        obecna_lista[wynik2[0]] = '*'

    print(f'Pozostałe próby: {licznik_prob}')

print('Niestety skończyły Ci się próby :(')
print('Tablica wyglądała następująco:')

t = baza.stworz_tablice(baza.lista_znakow, baza.ILE_RZEDOW, baza.ILE_KOLUMN)
baza.wyswietl_tablice(t, baza.ILE_RZEDOW, baza.ILE_KOLUMN)
