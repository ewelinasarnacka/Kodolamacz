
## WYZWANIE 5A - struktura wyrażeń arytmetycznych
### https://www.kodolamacz.pl/blog/wyzwanie-python-5-zaawansowane-aspekty-programowania-obiektowego/

import math
from abc import ABC, abstractmethod

class Wezel(ABC):

    @abstractmethod
    def nazwa(self):
        pass

    def wypisz(self):
        print("Wykonane działanie: " + self.nazwa())

    @abstractmethod
    def wartosc(self):
        pass


class Liczba(Wezel):
    def __init__(self, liczba):
        self.liczba = liczba

    def nazwa(self):
        return "liczba"

    def wypisz(self):
        print(f"Jestem liczbą {self.liczba}")

    def wartosc(self):
        return self.liczba


class Suma(Wezel):
    def __init__(self, skladnik1, skladnik2):
        self.skladnik1 = skladnik1
        self.skladnik2 = skladnik2

    def nazwa(self):
        return "dodawanie"

    def wypisz(self):
        self.skladnik1.wypisz()
        self.skladnik2.wypisz()
        super().wypisz()
        print(f"\t\t{self.skladnik1.wartosc()}+{self.skladnik2.wartosc()}={self.wartosc()}")

    def wartosc(self):
        return self.skladnik1.wartosc() + self.skladnik2.wartosc()

def main():

    cztery = Liczba(4)
    piec = Liczba(5)
    siedem = Liczba(7)
    osiem = Liczba(8)

    dodawanie = Suma(piec, siedem)
    dodawanie.wypisz()

if __name__ == "__main__":
    main()