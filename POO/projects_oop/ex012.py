# Criar uma classe para representar um Círculo e calcular a área e perímetro do mesmo.
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2

    def perimetro(self):
        return 2 * math.pi * self.raio

circulo = Circulo(5)
print(circulo.area())
print(circulo.perimetro())
