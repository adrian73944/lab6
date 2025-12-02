import time
def sekundik(czas):
    while czas > 0:
        print("Pozostały czas w sek: ",czas)
        time.sleep(1)
        czas -= 1
    print("Koniec czasu")

czas=int(input("Podaj czas: "))
sekundik(czas)