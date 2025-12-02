import math
import keyword

def wypisz_funkcje(obiekt):
    atrybuty = dir(obiekt)
    funkcje = []
    for atrybut in atrybuty:
        wartosc = getattr(obiekt, atrybut)
        if callable(wartosc):
            funkcje.append(atrybut)

    print((funkcje),',')

print("math: ")
wypisz_funkcje(math)
print("keyword:")
wypisz_funkcje(keyword)
print("tuple:")
wypisz_funkcje(tuple)