
## WYZWANIE 6B - zliczanie linii
### https://www.kodolamacz.pl/blog/wyzwanie-python-6-wyjatki-oraz-operacje-na-plikach/


import os

input("Podaj ścieżkę do pliku wejściowego:\n")
input("Podaj ścieżkę do pliku wyjściowego:\n")

def pobierz_sciezki():
    sciezka_do_odczytu = r"/Users/ewelina/Desktop/Test/Plik_wejsciowy.txt"
    sciezka_do_zapisu = r"/Users/ewelina/Desktop/Test/Test"
    return sciezka_do_odczytu, sciezka_do_zapisu
def wyswietl_sciezki():
    sciezka_do_odczytu = r"/Users/ewelina/Desktop/Test/Plik_wejsciowy.txt"
    sciezka_do_zapisu = r"/Users/ewelina/Desktop/Test/Test"
    print("Lokalizacja pliku wejściowego:\n\t" + sciezka_do_odczytu)
    print("Lokalizacja pliku wyjścowego:\n\t" + sciezka_do_zapisu)
def wczytaj_plik():
    file_to_open = pobierz_sciezki()
    with open(file_to_open[0]) as f:
        contents = f.read()
        print(contents)
def count_lines():
    file_to_open = pobierz_sciezki()
    count_lines = len(open(file_to_open[0]).readlines())
    print("Zliczenie linii w pliku")
    print("Plik wejściowy: " + file_to_open[0])
    print("Plik wejściowy zawiera " + str(count_lines) + " linii.")
    return count_lines
def zapisz_plik():
    path = pobierz_sciezki()
    file_to_read = path[0]
    file_to_save = path[1] + "/Plik_wyjsciowy.txt"
    to_save = count_lines()
    file = open(file_to_save, "w")
    file.write("Plik wejściowy: " + file_to_read + "\n")
    file.write("Plik wejściowy zawiera " + str(to_save) + " linii.")
def wczytaj_plik2():
    print("Zawartość pliku wyjściowego:")
    with open(r"/Users/ewelina/Desktop/Test/Test/Plik_wyjsciowy.txt") as f:
        contents = f.read()
        print(contents)

def main():
    #pobierz_sciezki()
    #print("\n")
    #wyswietl_sciezki()
    #wczytaj_plik()
    #print("\n")
    #count_lines()
    #zapisz_plik()
    wczytaj_plik2()
if __name__ == "__main__":
    main()