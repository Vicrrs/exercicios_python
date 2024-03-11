# Definição de Classe e Criação de Instância
class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Ana", 22)

print(pessoa1.nome)# Acessando o atributo nome da instância pessoa1
print(pessoa1.idade)# Acessando o atributo idade da instância pessoa1
