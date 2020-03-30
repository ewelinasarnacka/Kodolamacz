
# WYZWANIW 3B - palidromy
### https://www.kodolamacz.pl/blog/wyzwanie-python-3-algorytmy-i-struktury-danych/

import unittest

print("################ Czy Palindrom ################")

def czyPalindrom(text):
    print("Sprawdzenie, czy podany argument jest palindromem.")
    text = text.upper().replace(' ', '')
    r_string = text[::-1]
    if text == r_string:
        print("Podany argument ('%s') jest palindromem" % text)
        return "Tak"
    else:
        print("Podany argument ('%s') nie jest palindromem" % text)
        return "Nie"

czyPalindrom("2kajak2")
czyPalindrom("Kobyła ma mały bok")

class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert czyPalindrom("Kajak") == "Tak"
    def testSimpleCase_2(self):
        assert czyPalindrom("@Kajak@") == "Tak"
    def testSimpleCase_3(self):
        assert czyPalindrom("Kajak!") == "Nie"
    def testSpaces(self):
        assert czyPalindrom("Kobyła ma mały bok") == "Tak"

if __name__ == "__main__":
    unittest.main()

