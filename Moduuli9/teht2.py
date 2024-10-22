class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteitunnus = rekisteritunnus
        self.huippunopeus = float(huippunopeus)
        self.nopeus = float(nopeus)
        self.matka = float(matka)

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += float(nopeuden_muutos)
        if float(self.nopeus) <= 0:
            self.nopeus = 0
        elif float(self.nopeus) >= float(self.huippunopeus):
            self.nopeus = self.huippunopeus
        return

auto1 = Auto("ABC-123","142")

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f"Rekisterinumero: {auto1.rekisteitunnus}\nHuippunopeus: {auto1.huippunopeus}KM/H\nNopeus: {auto1.nopeus}KM/H\nMatka: {auto1.matka}KM")

auto1.kiihdytä(-200)

print(f"Rekisterinumero: {auto1.rekisteitunnus}\nHuippunopeus: {auto1.huippunopeus}KM/H\nNopeus: {auto1.nopeus}KM/H\nMatka: {auto1.matka}KM")
