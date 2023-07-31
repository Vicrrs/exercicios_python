# Sobrescrever método na classe derivada
class Animal:
    def emitir_som(self):
        return "Som indeterminado!"

class Cachorro:
    def emitir_som(self):
        return "AU AU"

class Gato(Animal):
    def emitir_som(self):
        return "MIAU"

cachorro = Cachorro()
gato = Gato()
print(cachorro.emitir_som()) # Saída: "Au au!"
print(gato.emitir_som())     # Saída: "Som indeterminado"
