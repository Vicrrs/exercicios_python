# Polimorfismo
"""
Polimorfismo é demonstrado pelo fato de que diferentes classes (Cachorro e Gato), 
ambas subclasses de Animal, implementam o método falar de maneira diferente. 
A função ouvir_animal pode invocar falar em qualquer instância de Animal (ou subclasses), 
mostrando diferentes comportamentos (sons) dependendo da classe da instância.
"""

class Animal:
    def falar(self):
        return "Algum som"
    
class Cachorro(Animal):
    def falar(self):
        return "AuAu!"
    
class Gato(Animal):
    def falar(self):
        return "MIAU!"
    
def ouvir_animal(animal):
    print(animal.falar())
    
ouvir_animal(Cachorro())
ouvir_animal(Gato())
