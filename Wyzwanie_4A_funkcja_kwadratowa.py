
## WYZWANIE 4A - funkcja kwadratowa
### https://www.kodolamacz.pl/blog/wyzwanie-python-4-rozwiazanie/

import unittest
import math

print("################ Funkcja kwadratowa ################")

class FunkcjaKwadratowa:
    y = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def delta(self):
        delta = self.b * self.b - 4 * self.a * self.c
        return delta
    def print_data(self):
        print(f"Postać funkcji:\n\tf(x) = {self.a}x^2 + {self.b}x + {self.c}\nDelta = {self.delta()}")
    def rozwiaz(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return "Nieskończenie wiele miejsc zerowych"
            #return float("inf")
        elif self.a == 0 and self.b == 0 and self.c != 0:
            return "Brak miejsca zerowego"
            #return float("nan")
        elif self.a == 0:
            x1 = round(-self.c / self.b,3)
            return x1
        elif self.delta() < 0:
            return "Brak miejsca zerowego"
        elif self.delta() == 0:
            x1 = round(-self.b / (2 * self.a),3)
            return x1
        elif self.delta() > 0:
            x1 = round((-self.b + math.sqrt(self.delta()))/ (2 * self.a),3)
            x2 = round((-self.b - math.sqrt(self.delta()))/ (2 * self.a),3)
            return x1, x2
    def print_score(self):
        print(f"Rozwiązanie: {self.rozwiaz()}")

def main(a, b, c):
    Dane =  FunkcjaKwadratowa(a, b, c)
    Dane.delta()
    Dane.print_data()
    Dane.rozwiaz()
    Dane.print_score()

if __name__ == "__main__":
    main(0, 0, 0)
    main(0, 0, -2)
    main(-5, 6, -2)
    main(2, -4, 2)
    main(-1, 3, 4)
    main(0, 3, 4)


"""
class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert main(0, 0, 0) == "X zawiera sie w R"

if __name__ == "__main__":
    unittest.main()
"""