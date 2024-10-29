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

    def tulosta_tiedot(self):
        print(f"Autolla {self.rekisteritunnus} mittarilukema on {self.matka}.")

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kwh, nopeus=0, matka=0):
        self.akkukapasiteetti_kwh = akkukapasiteetti_kwh
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko, nopeus=0, matka=0):
        self.tankin_koko = tankin_koko
        super().__init__(rekisteritunnus, huippunopeus)

autot = []

autot.append(Sähköauto("ABC-15", 180, "52.5KW/H"))
autot.append(Polttomoottoriauto("ACD-15", 165, "32.3L"))

for auto in autot:
    auto.kiihdytä(random.randint(1, 150))
    auto.kulje(3)
    auto.tulosta_tiedot()
