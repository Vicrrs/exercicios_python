# Encapsulamento
class Computador:
    def __init__(self):
        self. __max_preco = 1000

    def vender(self):
        print(f"Vendendo por {self.__max_preco}")

    def set_max_preco(self, preco):
        if preco > 1000:
            print("Preco maximo nao pode exceder 1000.")
        else:
            self.__max_preco = preco

# Testando o encapsulamento
pc = Computador()
pc.vender()

# Tentando alterar o preço
pc.set_max_preco(900)
pc.vender()
