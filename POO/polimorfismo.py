# Polimorfismo
class Passaro:
    def voar(self):
        print("Alguns pássaros podem voar!")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar!")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao voa!")

# Testando Polimorfismo
passaro = Passaro()
pardal = Pardal()
avestruz = Avestruz()

passaro.voar()
pardal.voar()
avestruz.voar()
