import random

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

autot = []
for i in range(10):
    auto = Auto(f"ABC-{Auto.tehty + 1}", random.randint(100, 200))
    autot.append(auto)

pisin_matka = 0
while pisin_matka < 10000:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
    for auto in autot:
        auto.kulje(1)
    for auto in autot:
        if auto.matka > pisin_matka:
            pisin_matka = auto.matka

for auto in autot:
    print(f"Rekisterinumero: {auto.rekisteritunnus}\nHuippunopeus: {auto.huippunopeus}KM/H\nNopeus: {auto.nopeus}KM/H\nMatka: {auto.matka}KM\n")



