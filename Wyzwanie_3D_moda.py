
# WYZWANIW 3D - moda
### https://www.kodolamacz.pl/blog/wyzwanie-python-3-algorytmy-i-struktury-danych/

import unittest

print("################ Najczęściej występująca liczba ################")

def moda(lista_liczb):
    print("Sprawdzenie, która liczba występuje na liście najczęściej.")
    lista_liczb = [a for a in lista_liczb if type(a) is int]
    set_lista_liczb = set(lista_liczb)

    lista_count = []
    slonik_lista_count = {}
    for liczba in set_lista_liczb:
        count_liczba = lista_liczb.count(liczba)

        lista_count.append(count_liczba)
        slonik_lista_count[liczba] = count_liczba

    max_czestosc = max(lista_count)
    wynik = []

    for kay, value in slonik_lista_count.items():
         if value == max_czestosc:
             wynik.append(kay)
             print(kay)
    wynik_last = wynik[0]
#    return wynik_last
    print("WYNIK: ")
    print(wynik_last)
moda([1,2,3,4,3,2,2,4,4,7,"m","m","m", 2.5, 2.5, 2.5])

"""
class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert moda([1,2,3,4,3,2,2,4,4,7,"m","m","m", 2.5, 2.5, 2.5]) == "2"

if __name__ == "__main__":
    unittest.main()
"""