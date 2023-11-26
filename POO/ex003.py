from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def informacoes_basicas(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}"

    @abstractmethod
    def descricao(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas

    def descricao(self):
        return f"Carro {self._modelo}, com {self.numero_portas} portas"


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga

    def descricao(self):
         return f"Caminhão {self._modelo}, com {self.capacidade_carga} toneladas"


class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def descricao(self):
        return f"Motocicleta {self._modelo}, com motor {self.tipo_motor}"


# Exemplo de uso
carro = Carro("Toyota", "Corolla", 2020, 4)
print(carro.descricao())

caminhao = Caminhao("Volvo", "FH", 2018, 20)
print(caminhao.descricao())

moto = Motocicleta("Honda", "CB500", 2021, "4 tempos")
print(moto.descricao())
