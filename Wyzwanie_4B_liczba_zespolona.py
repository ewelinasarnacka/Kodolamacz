
## WYZWANIE 4A - liczba zespolona
### https://www.kodolamacz.pl/blog/wyzwanie-python-4-rozwiazanie/

import unittest
import math

print("################ Liczba zespolona ################")

class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def wypisz(self):
        if self.im < 0:
            print(f"Liczba zespolona: z=={self.re}{self.im}i")
        else:
            print(f"Liczba zespolona: z={self.re}+{self.im}i")
    def modul(self):
        zm = math.sqrt(self.re ** 2 + self.im ** 2)
        return zm
    def print_module(self):
        if self.im < 0:
            print(f"Moduł liczby zespolonej z={self.re}{self.im}i to: {self.modul()}")
        else:
            print(f"Moduł liczby zespolonej z={self.re}+{self.im}i to: {self.modul()}")
    @staticmethod
    def dodaj(z1,z2):
        re_sum = z1.re + z2.re
        im_sum = z1.im + z2.im
        return Zespolona(re_sum, im_sum)
    @staticmethod
    def mnoz(z1,z2):
        re_multi = (z1.re * z2.re) - (z1.im * z2.im)
        im_multi = (z1.re * z2.im) + (z1.im * z2.re)
        return (re_multi, im_multi)

def main():
    z1 = Zespolona(3, 4)
    z2 = Zespolona(1, 1)
    z1.wypisz()
    z2.wypisz()
    z1.modul
    z1.print_module()
    Zespolona.dodaj(z1,z2).wypisz()
    Zespolona.dodaj(z1,z2).print_dodaj()
if __name__ == "__main__":
    main()


"""
class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert main(0, 0, 0) == "X zawiera sie w R"

if __name__ == "__main__":
    unittest.main()
"""