# Criar uma classe para representar um Retângulo e verificar se ele é um quadrado (todos os lados iguais).
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def e_quadrado(self):
        return self.comprimento == self.largura


retangulo1 = Retangulo(5, 5)
retangulo2 = Retangulo(3, 6)
print(retangulo1.e_quadrado())
print(retangulo2.e_quadrado())
