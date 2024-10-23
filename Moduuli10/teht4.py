import random
from operator import truediv, truth


class Auto:
    tehty = 0
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        self.nopeus = int(nopeus)
        self.matka = int(matka)
        Auto.tehty += 1

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += int(nopeuden_muutos)
        if int(self.nopeus) <= 0:
            self.nopeus = 0
        elif int(self.nopeus) >= int(self.huippunopeus):
            self.nopeus = self.huippunopeus
        return

    def kulje(self, tuntia):
        self.matka += int(tuntia) * int(self.nopeus)

class Kilpailu:
    def __init__(self, nimi, pituus, autot=[]):
        self.autot = autot
        self.nimi = nimi
        self.pituus = pituus

    pisin_matka = 0
    tuntia = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
        for auto in self.autot:
            auto.kulje(1)
        for auto in self.autot:
            if auto.matka > self.pisin_matka:
                self.pisin_matka = auto.matka
        self.tuntia += 1

    def tulosta_tilanne(self):
        if self.tuntia % 10 == 0:
            for auto in self.autot:
                print(f"Rekisterinumero: {auto.rekisteritunnus}\nHuippunopeus: {auto.huippunopeus}KM/H\nNopeus: {auto.nopeus}KM/H\nMatka: {auto.matka}KM\n")
            print(f"Tunteja kulunut:{self.tuntia}\n")
        elif self.pisin_matka > self.pituus:
            for auto in self.autot:
                print(f"Rekisterinumero: {auto.rekisteritunnus}\nHuippunopeus: {auto.huippunopeus}KM/H\nNopeus: {auto.nopeus}KM/H\nMatka: {auto.matka}KM\n")
            print(f"Tunteja kului:{self.tuntia}")
        return

    def kilpailu_ohi(self):
        if self.pisin_matka > self.pituus:
            return True
        else:
            return False


autot = []
for i in range(10):
    auto = Auto(f"ABC-{Auto.tehty + 1}", random.randint(100, 200))
    autot.append(auto)

k = Kilpailu("Suuri_romuralli", 8000, autot)

while k.kilpailu_ohi() == False:
    k.tunti_kuluu()
    k.tulosta_tilanne()
    k.kilpailu_ohi()






