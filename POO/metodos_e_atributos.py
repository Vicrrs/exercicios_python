# Metodos e atributos
class Animal:
    def __init__(self, especie):
        self.especie = especie

    def fazer_som(self, som):
        print(f"Este {self.especie} faz '{som}'")

# Usando a classe
gato = Animal("gato")
gato.fazer_som("miau")
