# Herança
class Veiculo:
    def __init__(self, marca) -> None:
        self.marca = marca
    
    def buzinar(self):
        return "Beep!"
    
class Carro(Veiculo): # Heranca
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca) # Chamada ao construtor da superclasse
        self.modelo = modelo
        
carro = Carro("Toyota", "Corolla")
print(carro.marca)
print(carro.modelo)  
print(carro.buzinar())  # Acesso ao método da superclasse
    