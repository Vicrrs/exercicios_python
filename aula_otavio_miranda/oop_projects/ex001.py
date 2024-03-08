# Métodos e instancias de classes em python
# Classe é um molde que gera novas instancias/objetos

# Método é uma funcao que esta dentro de uma classe
# self é o mesmo que o objeto fora da caixa

# Classe - Molde (geralmente sem dados)
# Instancia da class (objeto) - tem dados
# Na classe o self é apropria instancia.

class Carro:          # nome é um parametro no meu init
    def __init__(self, nome): # self : eu mesmo, intancia da classe
        self.nome = nome
        
    def acelerar(self): # Um método é um funcao que esta dentro da classe
        return f"{self.nome} está acelerando..."
        
        
fusca = Carro('Fusca')
print(fusca.nome)
print(fusca.acelerar())
