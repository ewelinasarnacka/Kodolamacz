
## WYZWANIE 6C - sprzątanie
### https://www.kodolamacz.pl/blog/wyzwanie-python-6-wyjatki-oraz-operacje-na-plikach/


import os
import datetime
import glob
import smtplib
import string

def pobierz_sciezke():
 #   input("Podaj ścieżkę do folderu z plikami:\n")
    sciezka_do_folderu = r"/Users/ewelina/Desktop/Test"
 #   print("Lokalizacja plików:\n\t" + sciezka_do_folderu)
    return sciezka_do_folderu

def pobierz_pliki():
    sciezka_do_folderu = pobierz_sciezke()
    list_of_files = (os.listdir(sciezka_do_folderu))
    try:
        list_of_files.remove(".DS_Store")
    except:
        pass
    print("Lokalizacja plików:\n\t" + sciezka_do_folderu)
    print("Lista plików we wskazanym folderze:\n\t" + '\n\t'.join(list_of_files))
    return list_of_files

def wybierz_pliki():
    sciezka_do_folderu = pobierz_sciezke()
    list_of_files = pobierz_pliki()
    now = datetime.datetime.today()  # Get current date
    creation_dates = []
    dif_dates =[]
    list_of_files_to_del = {}
    for file in list_of_files:
        creation_date = os.stat(sciezka_do_folderu + "/" + file).st_ctime # get creation datetime
        creation_date = datetime.datetime.fromtimestamp(creation_date) # nadaje format daty
        creation_dates.append(creation_date)

        dif = now - creation_date  # calculating days between actual date and last creation date
        dif_dates.append(dif)

        size_kb = os.path.getsize(sciezka_do_folderu + "/" + file)/1000
        if dif  > datetime.timedelta(minutes = 100) and size_kb > 50:
            list_of_files_to_del[file] = (creation_date, dif, size_kb)
        else:
            pass
    print("Lista plików do usunięcia:")
    for a in list_of_files_to_del:
        print("\t" + "nazwa pliku:  " + a + "\n\t\tdata pliku: " + str(list_of_files_to_del[a][0]) + "\n\t\twiek pliku: " + str(list_of_files_to_del[a][1]) + "\n\t\twielkość pliku: " + str(list_of_files_to_del[a][2]))
    return list_of_files_to_del

def usuniecie_plikow():
    sciezka_do_folderu = pobierz_sciezke()
    list_of_files_to_del = wybierz_pliki()
    potwierdzenie = input("Jeśli potwierdzasz usunięcie plików wpisz 'Yes':\n")
    if potwierdzenie.upper() == "YES":
        #for file in list_of_files_to_del:
        #    os.remove(sciezka_do_folderu + "/" + file)
        print("Wybrane pliki zostały usunięte.\n")
    else:
        print("Operacja usuwania plików została anulowana.")
    print("W folderze pozostały pliki:\n\t" + '\n\t'.join(os.listdir(sciezka_do_folderu)))

def main():
    pobierz_sciezke()
    pobierz_pliki()
    wybierz_pliki()
    usuniecie_plikow()
if __name__ == "__main__":
    main()