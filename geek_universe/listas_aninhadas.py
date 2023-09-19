"""
Listas Aninhadas (nested list)

- Unidimensionais (arrays/vetores)
- Multidimensionais (matrizes)
"""

# Exemplo 1
print("Exemplo 1: ")

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
print(type(listas))

# Acessando os dados
print(listas[0])
print(listas[0][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    print(lista)

print("-=-"*10)

for lista in listas:
    for num in lista:
        print(num)

print("-=-"*10)

# Lista Comprehension
[[print(valor) for valor in lista] for lista in listas]

print("-=-"*10)
print("Gerando um tabuleiro")
print("-=-"*10)

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

print("-=-"*10)
print("Gerando jogadas para jogo da velha")
print("-=-"*10)

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)


print("Gerando um valor qualquer")
print([['*' for i in range(1, 4)] for j in range(1, 4)])
