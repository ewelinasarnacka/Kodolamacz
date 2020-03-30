
## WYZWANIE 5A - Figury geometryczne
### https://www.kodolamacz.pl/blog/wyzwanie-python-5-zaawansowane-aspekty-programowania-obiektowego/

import math
from abc import ABC, abstractmethod

class Figury(ABC):

    @abstractmethod
    def nazwa(self):
        pass
    @abstractmethod
    def oblicz_obwod(self):
        pass
    @abstractmethod
    def oblicz_pole(self):
        pass

    def print_wyniki(self):
        #print("Figura geometyczna: " + self.nazwa())
        print("Wyniki obliczeń:\n\t Obwód = " + str(self.oblicz_obwod()) + "\n\t Pole = " + str(self.oblicz_pole()))

class Kola(Figury):
    pi = math.pi
    def __init__(self, promien):
        self.promien = promien
    def nazwa(self):
        return "koło"
    def print_dane(self):
        print("Typ: " + self.nazwa() + "\nDane:" + "\n\tPromień = " + str(self.promien))
    def oblicz_obwod(self):
        if self.promien <= 0:
            return "Błędne dane wejściowe"
        else:
            obwod = 2 * self.pi * self.promien
            return round(obwod, 3)
    def oblicz_pole(self):

        if self.promien <= 0:
            return "Błędne dane wejściowe"
        else:
            pole = self.pi * self.promien * self.promien
            return round(pole, 3)

class Trojkaty(Figury):
    def __init__(self, podstawa, bok2, bok3, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc
        self.bok2 = bok2
        self.bok3 = bok3
    def nazwa(self):
        return "trojkąt"
    def print_dane(self):
        print("Typ: " + self.nazwa() + "\nDane:" + "\n\tPodstawa = " + str(self.podstawa) + ":\n\tSzciana 2 = " + str(round(self.bok2,3)) + ":\n\tSzciana 3 = " + str(round(self.bok3,3)))
    def oblicz_obwod(self):
        obwod = self.wysokosc + self.bok2 + self.bok3
        return round(obwod, 3)
    def oblicz_pole(self):
        pole = 0.5 * self.podstawa * self.wysokosc
        return round(pole, 3)

class Kwadraty(Figury):
    def __init__(self, dlugosc):
        self.dlugosc = dlugosc

    @property
    def dlugosc(self):
        return self.__dlugosc
    @dlugosc.setter
    def dlugosc(self,dlugosc):
        if dlugosc < 0:
            self.__dlugosc = 0
            #raise Exception("Długość ściany kwadratu nie może być mniejsze od 0")
            print("Długość ściany kwadratu nie może być mniejsze od 0")
        else:
            self.__dlugosc = dlugosc

    def nazwa(self):
        return "kwadrat"
    def print_dane(self):
        print("Typ: " + self.nazwa() + "\nDane:" + "\n\tDługość = " + str(
            round(self.dlugosc, 3)))
    def oblicz_obwod(self):
        obwod = 4 * self.dlugosc
        return round(obwod, 3)
    def oblicz_pole(self):
        pole = self.dlugosc * self.dlugosc
        return round(pole, 3)

class Prostokaty(Kwadraty):
    def __init__(self, dlugosc, szerokosc):
        super().__init__(dlugosc)
        self.szerokosc = szerokosc
    def nazwa(self):
        return "prostokąt"
    def print_dane(self):
        print("Typ: " + self.nazwa() + "\nDane:" + "\n\tDługość = " + str(round(self.dlugosc,3)) + ":\n\tSzerokość = " + str(round(self.szerokosc,3)))
    def oblicz_obwod(self):
        if self.dlugosc <= 0 or self.szerokosc <= 0:
            return "Błędne dane wejściowe"
        else:
            obwod = 2 * self.dlugosc + 2 * self.szerokosc
            return round(obwod, 3)
    def oblicz_pole(self):
        if self.dlugosc <= 0 or self.szerokosc <= 0:
            return "Błędne dane wejściowe"
        else:
            pole = self.dlugosc * self.szerokosc
            return round(pole, 3)


def main():
    Kolo_1 = Kola(2)
    Kolo_1.print_dane()
    Kolo_1.print_wyniki()

    Trojkat_1 = Trojkaty(10, math.sqrt(41), math.sqrt(41) , 4)
    Trojkat_1.print_dane()
    Trojkat_1.print_wyniki()

    Kwadrat_1 = Kwadraty(5)
    Kwadrat_1.print_dane()
    Kwadrat_1.print_wyniki()

    Prostokat_1 = Prostokaty(2, -6)
    Prostokat_1.print_dane()
    Prostokat_1.print_wyniki()

if __name__ == "__main__":
    main()