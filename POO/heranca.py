# Heranca
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

# Usando heranca
meu_carro = Carro("Honda", "Civic")
print(f"Marca:{meu_carro.marca}, Modelo: {meu_carro.modelo}")
