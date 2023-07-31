# Criar uma classe abstrata (utilizando a biblioteca abc)

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

retangulo = Retangulo(5, 10)
print(retangulo.area())
