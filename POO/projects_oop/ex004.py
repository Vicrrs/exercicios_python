#  Adicionar um atributo estático à classe Pessoa
class Pessoa:
    total_pessoas = 0

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

pessoa1 = Pessoa("Victor", 23)
pessoa2 = Pessoa("Jaque", 24)
print(Pessoa.total_pessoas)
