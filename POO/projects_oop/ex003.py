#  Criar uma classe com herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som identificado"

class Cachorro(Animal):
    def emitir_som(self):
        return "AU AU!"

cachorro  = Cachorro("Rex")
print(cachorro.emitir_som())
