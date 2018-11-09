#kwadrat liczby
liczba = input("Podaj liczbe: ")
liczba = int(liczba)

print(liczba*liczba)
#potęga liczby
liczba = input("Podaj liczbe: ")
liczba = int(liczba)

potega = input("Podaj potege: ")
potega = int(potega)

odpowiedz = liczba # ^1 potega

for i in range(1, potega):
    odpowiedz*=liczba
    print("potega ",odpowiedz)

#ile liter 'b' w texcie

#ile liter głośnych w texcie

#pora roku
#wejscie => miesiąc 0..12
#wejście "zima, wiosna, lato, jesień"
miesiac = input("Podaj miesiac: ")
miesiac = int(miesiac)
if miesiac<3:
    print("zima")
if miesiac<6:
    print("wiosna")
if miesiac<9:
    print("lato")
if miesiac<11:
    print("jesien")
else:
    print("zima")

#poprawna data
#wejscie => dzien miesiac rok
#wyjscie => true, false (niepoprawny dzien, miesiac, rok)
miesiac = input("Podaj miesiac: ")
miesiac = int(miesiac)
# ====================================

# depozyt
#wejscie => ilość pieniądze którą dajemy do banku, czas (lat) ile trzymamy pieniądze na depozycie
#wejście (n razy czas przechowywania pieniądze) np 1000 => 1010 => 1022 itp (+10%)

pieniadze = input("Podaj pieniadze na rachunek: ")
czas = input("Za ile lat zabierzesz pieniadze z banku?: ")

czas = int(czas)
pieniadze = float(pieniadze)

for rok in range(czas):
    pieniadze *=1.1
    print("kwota = ", pieniadze)

#rok przestępny
#wejscie => rok np 1997
#wyjście true jeżeli tak, false jeżeli nie