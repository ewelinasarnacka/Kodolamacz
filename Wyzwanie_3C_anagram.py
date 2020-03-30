
# WYZWANIW 3C - anagramy
### https://www.kodolamacz.pl/blog/wyzwanie-python-3-algorytmy-i-struktury-danych/

import unittest

def clean(word):
    returnword = ""
    for letter in word.lower():
        if letter >= 'a' and letter <='z':
            # not out of bounds
            returnword += letter
    return returnword

#clean("had34028** dsaA")

print("################ Czy Anagram ################")

def czyAnagram(string_1a, string_2a):
    print("Sprawdzenie, czy podane argumenty są anagramem.")

    string_1 = clean(string_1a)
    string_2 = clean(string_2a)
    string_1 = string_1.upper().replace(" ", "")
    string_2 = string_2.upper().replace(" ", "")

    lista_str_1 = sorted(list(string_1))
    lista_str_2 = sorted(list(string_2))

#    print(lista_str_1)
#    print(lista_str_2)

    if lista_str_1 == lista_str_2:
        print("Podane argumenty ('%s', '%s') są anagramem." % (string_1a, string_2a))
        return "Tak"
    else:
        print("Podane argumenty ('%s', '%s') nie są anagramem." % (string_1a, string_2a))
        return "Nie"

czyAnagram("Vladimir Nabokov", "Vivian Darkbloom")
czyAnagram("Quid est veritas?", "Vir est qui adest")
czyAnagram("Quid est veritas?", "Vir est qui adestt")


class ExpTestCase(unittest.TestCase):

    def testSimpleCase_1(self):
        assert czyAnagram("Vladimir Nabokov", "Vivian Darkbloom") == "Tak"
    def testSimpleCase_2(self):
        assert czyAnagram("Quid est veritas?", "Vir est qui adest") == "Tak"
    def testSimpleCase_3(self):
        assert czyAnagram("Vladimir Nabokov", "Vivien Darkbloom") == "Nie"
    def testSimpleCase_4(self):
        assert czyAnagram("Vladimir Nabokov", "Viviaan Darkbloom") == "Nie"

if __name__ == "__main__":
    unittest.main()
