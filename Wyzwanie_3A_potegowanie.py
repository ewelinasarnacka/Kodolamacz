
# WYZWANIW 3A - sprytne obliczanie potęgi
### https://www.kodolamacz.pl/blog/wyzwanie-python-3-algorytmy-i-struktury-danych/

import unittest

print("################ Sprytne pątegowanie ################")

def sprytne_potegowanie(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    elif wykladnik == 0:
        return 1
    else:
        pierwsza_potega = sprytne_potegowanie(podstawa,wykladnik//2)
        if (wykladnik) % 2 != 0:
            wynik = pierwsza_potega * pierwsza_potega * podstawa
            return wynik
        else:
            wynik = pierwsza_potega * pierwsza_potega
            return wynik

print(sprytne_potegowanie(2, 337))


class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert sprytne_potegowanie(2, 1) == 2
    def testSimpleCase_2(self):
        assert sprytne_potegowanie(2, 2) == 4
    def testSimpleCase_3(self):
        assert sprytne_potegowanie(3, 2) == 9
    def testSimpleCase_4(self):
        assert sprytne_potegowanie(2, 0) == 1
    def testSimpleCase_5(self):
        assert sprytne_potegowanie(2, 7) == 128
    def testSimpleCase_6(self):
        assert sprytne_potegowanie(2, 6) == 64

    @unittest.skip
    def testSimpleCase_7(self):
        assert sprytne_potegowanie(2, -1) == 1/2
    @unittest.skip
    def testSimpleCase_8(self):
        assert sprytne_potegowanie(2, -2) == 1/4
    @unittest.skip
    def testSimpleCase_9(self):
        assert sprytne_potegowanie(2, -3) == 1/8

    def testSimpleCase_10(self):
        assert sprytne_potegowanie(-2, 3) == -8
    def testSimpleCase_11(self):
        assert sprytne_potegowanie(-2, 4) == 16

if __name__ == "__main__":
    unittest.main()
