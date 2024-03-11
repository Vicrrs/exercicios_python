# Encapsulamento com Propriedades

"""
@property e @nome.setter são usados para criar uma propriedade nome com um getter e um setter, 
permitindo o controle sobre como o atributo privado __nome é acessado e modificado, encapsulando
a lógica de validação dentro da classe.
"""
class Pessoa:
    def __init__(self, nome) -> None:
        self.__nome = nome # Atributo privado
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self.__nome = valor
        else:
            raise ValueError("Nome deve ser uma string")

pessoa = Pessoa("Rafael")
pessoa.nome = "Gabriel"  # Acessa o setter
print(pessoa.nome)  # Acessa o getter
