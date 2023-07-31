# Adicionar um método à classe Pessoa
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

pessoa1 = Pessoa("Victor", 23)
print(pessoa1.saudacao())
