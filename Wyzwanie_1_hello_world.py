
## Wyzwanie 1
### https://www.kodolamacz.pl/blog/wyzwanie-python-1-hello-world/

def main():
    imie = input("Podaj swoje imię:\n" )
    nazwisko = input("Podaj swoje nazwisko:\n")
    print("Witaj " + imie.title() + " " + nazwisko.title())
if __name__ == "__main__":
    main()