
## WYZWANIE 4A - ułamek
### https://www.kodolamacz.pl/blog/wyzwanie-python-4-rozwiazanie/

import unittest
import math

print("################ Ułamek ################")

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.ulamek = round(self.licznik / self.mianownik,  5)
    def print_ulamek(self):
        print(f"Ułamek = {self.ulamek}; licznik = {self.licznik}, mianownik = {self.mianownik}")

    def divider(self):
        min_lm = min(self.licznik, self.mianownik)
        max_divider = 1
        for i in range(min_lm+1):
            if i > max_divider and self.licznik % i == 0 and  self.mianownik % i == 0:
                max_divider = i
        return max_divider
    def print_divider(self):
        print(f"Największy wspólny dzielnik = {self.divider()}")

    def skroc(self):
        licznik_skrocony = self.licznik / self.divider()
        mianownik_skrocony = self.mianownik / self.divider()
        return (licznik_skrocony, mianownik_skrocony)
    def print_skroc(self):
        print(f"Ułamek skrócony = {self.ulamek}; licznik = {self.skroc()[0]}, mianownik = {self.skroc()[1]}")

    def dzialania(self, other):
        licznik_sum = (self.licznik * other.mianownik) + (self.mianownik * other.licznik)
        mianownik_sum = self.mianownik * other.mianownik
        licznik_dif = (self.licznik * other.mianownik) - (self.mianownik * other.licznik)
        mianownik_dif = self.mianownik * other.mianownik
        licznik_multi =  self.licznik * other.licznik
        mianownik_multi = self.mianownik * other.mianownik
        licznik_div =  self.licznik * other.mianownik
        mianownik_div = self.mianownik * other.licznik
        return (licznik_sum, mianownik_sum, licznik_dif, mianownik_dif, licznik_multi,  mianownik_multi, licznik_div, mianownik_div)

    def ulamek_sum(self, other):
        ulamek_sum = round(self.dzialania(other)[0] / self.dzialania(other)[1], 5)
        return ulamek_sum
    def ulamek_dif(self, other):
        ulamek_dif = round(self.dzialania(other)[2] / self.dzialania(other)[3], 5)
        return ulamek_dif
    def ulamek_multi(self, other):
        ulamek_multi = round(self.dzialania(other)[4] / self.dzialania(other)[5], 5)
        return ulamek_multi
    def ulamek_div(self, other):
        if self.dzialania(other)[7] == 0:
            ulamek_div = "Error (dzielenie przez 0)"
        else:
            ulamek_div = round(self.dzialania(other)[6] / self.dzialania(other)[7], 5)
        return ulamek_div

    def print_sum(self, other):
        print(f"Suma ułamków = {self.ulamek_sum(other)}")
    def print_dif(self, other):
        print(f"Różnica ułamków = {self.ulamek_dif(other)}")
    def print_multi(self, other):
        print(f"Iloczyn ułamków = {self.ulamek_multi(other)}")
    def print_div(self, other):
        print(f"Iloraz ułamków = {self.ulamek_div(other)}")

def main():
    ulamek = Ulamek(122, 244)
    ulamek.print_ulamek()
    ulamek.print_divider()
    ulamek.print_skroc()
    ulamek2 = Ulamek(1, 3)
    ulamek2.print_ulamek()
    ulamek.dzialania(ulamek2)
    ulamek.print_sum(ulamek2)
    ulamek.print_dif(ulamek2)
    ulamek.print_multi(ulamek2)
    ulamek.print_div(ulamek2)
if __name__ == "__main__":
    main()


"""
class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert main(0, 0, 0) == "X zawiera sie w R"

if __name__ == "__main__":
    unittest.main()
"""