"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem
ter seus próprios atributos e métodos. Os objetos gerados
pela classe podem usar seus dados internos para realizar
várias ações. Por convenção, usamos PascalCase para nomes de classes.
"""

# string = "Victor" #str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Victor", "Roza")
p2 = Pessoa("Jaqueline", "Roza")

print(p1.nome)
print(p1.sobrenome)

