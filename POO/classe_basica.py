# Classe basica
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")


# Criando um objeto
meu_carro = Carro("Torota", "Corola")
meu_carro.exibir_info()
