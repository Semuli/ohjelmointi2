class Hissi:
    def __init__(self, alin, ylin, kerros=0):
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros
        self.kerros = self.alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on nyt {self.kerros}. kerroksesa")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on nyt {self.kerros}. kerroksesa")
        return

    def siirry_kerrokseen(self, kohde):
         while self.kerros > kohde:
             Hissi.kerros_alas(self)
         while self.kerros < kohde:
             Hissi.kerros_ylös(self)


h = Hissi(-5, 10)

h.siirry_kerrokseen(5)

h.siirry_kerrokseen(h.alin)