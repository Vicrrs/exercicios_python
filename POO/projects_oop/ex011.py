# Criar uma classe para representar um Ponto 2D e calcular a distância entre dois pontos.
import math

class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, outro_ponto):
        return math.sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)

ponto1 = Ponto2D(0, 0)
ponto2 = Ponto2D(3, 4)
print(ponto1.distancia(ponto2))
