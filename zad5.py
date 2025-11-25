import random
lista=list(range(1,50))
wynik=random.sample(lista,6)
wynik.sort()
print("Wygrywające liczby to: ", wynik)