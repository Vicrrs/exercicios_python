# Criando uma classe simples
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Victor", 23)
pessoa2 = Pessoa("Jaqueline", 24)

print(pessoa1)
print(pessoa1.nome)
print(pessoa1.idade)
