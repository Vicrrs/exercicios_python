"""
List Comprehension

Nós podemos adicionar logicas condicionais às list comprehensions
"""

# Exemplo 1
print("Exemplo 1: ")

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando
# "not" é uma palavra-chave que inverte o resultado. 
# Portanto, "not numero % 2" verifica se o número não é ímpar, ou seja, se ele é par.
pares1 = [numero for numero in numeros if not numero % 2]
impares1 = [numero for numero in numeros if numero % 2]

print(pares1)
print(impares1)


# Exemplo 2
print("Exemplo 2: ")

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)


