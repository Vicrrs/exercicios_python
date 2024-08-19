"""
Entendendo iterator e iterables

    - Iterable ->
        - Um iterable é qualquer objeto em python que pode ser iterado, ou seja, você pode percorrer seus elementos um a um. Exemplos de objetos iteraveis incluem listas, tuplas, strings, dicionarios, sets, entre outros.
        - Para que um objeto seja considerado um iterable, ele deve implementar o metodo especial '__iter()__', que retorna um iterator, ou implementar o metodo '__getitem__()' que permite acessar aos itens.

    - Iterator ->
        - Um iterator é um objeto que representa um fluxo de dados, permitindo que voce acesse seus elementos um por um, geralmente usando a funcao 'next()'. Para que um objeto seja cconsiderado um iterator, ele deve implementar os metodos especiais '__iter()__' e '__next()__'.
            - '__iter()__' retorna o proprio iterator (muitas vezes 'self').
            - '__next()__' retorna o proprio item da sequencia. Quando nao ha mais itens para retornar, ele lanca a excecao 'StopIteration'.


DIFERENÇA PRINCIPAL
    - ITERABLE: é um objeto que voce pode iterar sobre. Ele implementa o metodo '__iter()__' e retorna um iterator
    - ITERATOR: é o objeto que realiza a iteracao. Ele implementa os metodos '__iter()__' e '__next()__'.
"""


# Exemplo de um iterable
print("Exemplo de um iterable")
## Lista é um exemplo de iterable
lista = [1, 2, 3, 4, 5]

# Podemos usar um loop para iterar sobre a lista
for item in lista:
    print(item)


print('-=' * 10)


# Exemplo de um iterator
print("Exemplo de um iterator")
## Criando um iterator a partir de uma lista
lista = [1, 2, 3, 4, 5]
iterator = iter(lista) # A funcao iter() retorna um iterator

## Usando o metodo next() para acessar os itens um a um
print(next(iterator))
print(next(iterator))
print(next(iterator))

