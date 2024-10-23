class Hissi:
    def __init__(self, numero, alin, ylin, kerros=0):
        self.numero = numero
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros
        self.kerros = self.alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi {self.numero} on nyt {self.kerros}. kerroksesa")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi {self.numero} on nyt {self.kerros}. kerroksesa")
        return

    def siirry_kerrokseen(self, kohde):
         while self.kerros > kohde:
             Hissi.kerros_alas(self)
         while self.kerros < kohde:
             Hissi.kerros_ylös(self)

class Talo:
    def __init__(self, alin, ylin, hissejä):
        self.alin = alin
        self.ylin = ylin
        self.hissejä = hissejä

    hissejä_luotu = 0
    hissit = []

    def luo_hissejä(self, hissejä):
        for i in range(hissejä):
            h = Hissi(i, self.alin, self.ylin)
            Talo.hissit.append(h)
            Talo.hissejä_luotu += 1
        return

    def aja_hissiä(self, numero, kohde):
        Talo.hissit[numero].siirry_kerrokseen(kohde)


t = Talo(-5, 10, 12)
t.luo_hissejä(t.hissejä)

t.aja_hissiä(2, 5)
