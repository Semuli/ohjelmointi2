class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteitunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto1 = Auto("ABC-123","142KM/H")

print(f"Rekisterinumero: {auto1.rekisteitunnus}\nHuippunopeus: {auto1.huippunopeus}\nNopeus: {auto1.nopeus}KM/H\nMatka: {auto1.matka}KM")