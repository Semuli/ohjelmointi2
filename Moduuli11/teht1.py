class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_teidot(self):
        print(f"Julkaisu nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_teidot(self):
        super().tulosta_teidot()
        print(f"Kirjan kirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, pääkirjoittaja):
        self.pääkirjoittaja = pääkirjoittaja
        super().__init__(nimi)

    def tulosta_teidot(self):
        super().tulosta_teidot()
        print(f"Pääkirjoittaja: {self.pääkirjoittaja}")

lehti = Lehti("Aku ankka", "Aki Hyyppä")
lehti.tulosta_teidot()
print()
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", "200 sivua")
kirja.tulosta_teidot()