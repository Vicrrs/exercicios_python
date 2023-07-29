class Pessoa: # class que utilizamos para criar uma classe.
    def __init__(self, nome: str, idade: int, altura: float):
        # self utilizada para guardar a referência ao próprio objeto.
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}m")
        
    def cozinhar(self, receita: str):
        print(f"Estou cozinhando um(a): {receita}")
        
    def andar(self, distancia: float):
        print(f"Saí para andar. Volto quando completar {distancia}m")

# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome="Victor", idade=23, altura=1.69)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar("Lasanha")
pessoa.andar(800)
        