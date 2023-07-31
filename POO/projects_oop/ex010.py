# Criar uma classe com método estatico
class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

resultado = Calculadora.soma(10, 5)
print(resultado)
