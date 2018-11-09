import random

class smartphone():
    cena = None
    nazwa = 'noname'
    ram = None
    kamera = None

    def __init__(self, name, ram, kamera, price):
        self.cena = price
        self.nazwa = name
        self.ram = ram
        self.kamera = kamera

    def wypisz(self):
        print('Nazwa:', self.nazwa, ', ram: ', self.ram, 'Gb, kamera: ', self.kamera, 'megapixel, cena: ', self.cena)


class sklep():
    magazyn_smartfonow = []
    aparat_kasowy = 0

    def sprzedaj_smartfon(self):
        index_smartfonu = random.randint(0,len(self.magazyn_smartfonow)-1)

        smartfon_do_sprzedazy = self.magazyn_smartfonow[index_smartfonu]

        self.aparat_kasowy += smartfon_do_sprzedazy.cena

        print("sprzedano smartfon ")
        smartfon_do_sprzedazy.wypisz()

        self.magazyn_smartfonow.remove(smartfon_do_sprzedazy)


    def oblicz_kase(self):
        suma = 0

        for smarffon in self.magazyn_smartfonow:
            suma+=smarffon.cena

        print(suma)

    def wypisz_aparat_kasowy(self):
        print("W aparacie kasowym jest ", self.aparat_kasowy, " zlotych")

    def wypisz_wszystkie_smartfony(self):
        for smarffon in self.magazyn_smartfonow:
            smarffon.wypisz()

def wygeneruj_smarffon():
    cena = random.randint(1,1000)

    nazwy = ['iphone','nokia', 'samsung']
    i = random.randint(0,len(nazwy)-1)

    nazwa = nazwy[i]
    

    kamera = random.randint(1,20)

    rams = [1,2,3,4,6,8]
    ram = rams[random.randint(0,len(rams)-1)]

    sm = smartphone(nazwa, ram, kamera, cena)

    return sm


nasz_sklep = sklep()


for i in range(10):
    nowy_smartfon = wygeneruj_smarffon()
    nasz_sklep.magazyn_smartfonow.append(nowy_smartfon)


nasz_sklep.wypisz_aparat_kasowy()
print('\n') #wypisze na nowej linijce

nasz_sklep.sprzedaj_smartfon()
nasz_sklep.wypisz_aparat_kasowy()
print('\n') #wypisze na nowej linijce

nasz_sklep.sprzedaj_smartfon()
nasz_sklep.wypisz_aparat_kasowy()

print('\n') #wypisze na nowej linijce
print('pozostale smartfony:')
nasz_sklep.wypisz_wszystkie_smartfony()
