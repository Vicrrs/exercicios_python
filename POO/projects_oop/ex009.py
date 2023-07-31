# Utilizar o conceito de composição
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        return self.motor.ligar()

carro = Carro()
print(carro.ligar())
