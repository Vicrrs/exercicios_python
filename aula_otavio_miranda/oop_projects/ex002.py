# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome # atributos de instancia
        
    def comendo(self, alimento):
        return f"{self.nome} está comendo {alimento}"
        
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo(alimento="carne"))
