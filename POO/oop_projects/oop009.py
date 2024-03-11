# Métodos de Classe e Estáticos

"""
@staticmethod define um método estático somar que pode ser chamado na classe sem a necessidade de uma instância.
@classmethod define um método de classe dobrar que tem acesso à classe (cls) e pode chamar outros métodos da classe, incluindo métodos estáticos.
"""
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @classmethod
    def dobrar(cls, a):
        return cls.somar(a, a)
    
print(Matematica.somar(2, 3))  # Método estático chamado diretamente na classe
print(Matematica.dobrar(4))  # Método de classe que usa o método estático da própria classe
