
## WYZWANIE 2 - prosty kalkulator
### https://www.kodolamacz.pl/blog/wyzwanie-python-2-podstawowe-instrukcje/

def main():
    kolejne = "T"
    while kolejne in ("T"):
        print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę.")
        liczba_1 = input("Pierwsza liczba: \n")
        while True:
            try:
                liczba_1 = float(liczba_1)
                break
            except ValueError:
                liczba_1 = input("To nie jest liczba. Podaj jeszcze raz pierwszą liczbę: \n")
                continue
        operacja_m = input("Wtbierz operację matematyczną (+,-,*,/,%): \n")
        operacja_m = operacja_m.strip()
        while operacja_m not in ("+", "-", "*", "/", "%"):
            operacja_m = input("To nie jest operacja matematyczna. Podaj jeszcze raz operację matematyczną: \n")
            continue
        liczba_2 = input("Druga liczba: \n")
        while True:
            try:
                liczba_2 = float(liczba_2)
                break
            except ValueError:
                liczba_2 = input("To nie jest liczba. Podaj jeszcze raz drugą liczbę: \n")
                continue
        if operacja_m == "+":
            wynik = liczba_1 + liczba_2
            print("Twój wynik to: ", liczba_1, operacja_m, liczba_2, "=", round(wynik,2))
        if operacja_m == "-":
            wynik = liczba_1 - liczba_2
            print("Twój wynik to: ", liczba_1, operacja_m, liczba_2, "=", round(wynik,2))
        if operacja_m == "*":
            wynik = liczba_1 * liczba_2
            print("Twój wynik to: ", liczba_1, operacja_m, liczba_2, "=", round(wynik,2))
        if operacja_m == "%":
            wynik = liczba_1 % liczba_2
            print("Twój wynik to: ", liczba_1, operacja_m, liczba_2, "=", round(wynik,2))
        if operacja_m == "/" and liczba_2 != 0:
            wynik = liczba_1 / liczba_2
            print("Twój wynik to: ", liczba_1, operacja_m, liczba_2, "=", round(wynik,2))
        if operacja_m == "/" and liczba_2 == 0:
            print("ERROR: Nie dzielimy przez 0")
        kolejne = (input("Chcesz wykonać kolejne działanie? Wpisz literę t: \n"))
        kolejne = kolejne.upper()
    print("Koniec")
if __name__ == "__main__":
    main()