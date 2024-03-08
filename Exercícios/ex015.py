"""
is None: verifica se o valor de uma variável é exatamente None, que é um valor especial em Python utilizado para indicar a ausência de valor ou um valor "nulo". Utiliza-se essa expressão para testar explicitamente se uma variável não possui nenhum valor atribuído ou se foi definida para representar a ausência de um valor.

is not None: é o contrário de is None. Esta expressão verifica se uma variável possui um valor diferente de None. Ou seja, ela é utilizada para garantir que uma variável tenha algum valor atribuído que não seja None.


O operador is é utilizado em vez de == porque is compara as identidades dos objetos, não apenas seus valores. None é um singleton em Python, o que significa que existe apenas uma instância de None em qualquer momento da execução do programa. Portanto, is é a maneira correta de verificar se uma variável é None ou não.
"""

a = None

if a is None:
    print("a é None")
else:
    print("a não é None")
    
b = 5

if b is not None:
    print("b tem algum valor")
else:
    print("b é None")
