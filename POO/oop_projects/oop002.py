# Adicionando Métodos à Classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def se_apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!"

pessoa1 = Pessoa("Jack", 24)
print(pessoa1.se_apresentar()) # Invocando o método se_apresentar da instância pessoa1
