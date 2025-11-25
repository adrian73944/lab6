import datetime
lab=datetime.date(2025,11,18)
ile_minelo=datetime.date.today()-lab
liczba_dni=ile_minelo.days
print("Dni od ostatniego laboratorium:",liczba_dni)

kolokwium=datetime.date(2026,1,20)
ile_zostalo=kolokwium - datetime.date.today()
wynik_dni=ile_zostalo.days
print("Do kolokwium zostało:",wynik_dni,"dni")

