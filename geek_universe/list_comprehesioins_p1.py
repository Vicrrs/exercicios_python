"""
List Comprehesions

- Utilizando Comprehension nos podemos gerar novas listas com dados processados a partir
de outro iteravel

# Sintaxe da List Comprehension
[dado for dado in iteravel]
"""

# Exemplo1
print("Exemplo 1:")

numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 10 for numero in numeros]
print(res)

# Exemplo 2
print("Exemplo 2:")

numeros1 = [10, 20, 30, 40, 50, 60]

res1 = [numero // 2 for numero in numeros1]
print(res1)

# Exemplo 3
print("Exemplo 3:")

numeros2 = [3, 4, 5, 6, 7, 8]


def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros2]
print(res)

# Exemplo 4 - List Comprehension vs Loop
print("Exemplo 4:")

## Loop
# numeros3 = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    # numero_dobrado = numero * 2
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

## List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])


# Exemplo 5
print("Exemplo 5:")

nome = "Victor Roza"

print([letra.upper() for letra in nome])

# Exemplo 6
print("Exemplo 6:")

friends = ["williams", "thiago", "arcanjo", "xande", "vere", "chris", "serra"]

print([amigo[0].upper() for amigo in friends])


# Exemplo 7
print("Exemplo 7:")


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ["williams", "thiago", "arcanjo", "xande", "vere", "chris", "serra"]

print([caixa_alta(amigo) for amigo in amigos])


# Exemplo 8
print("Exemplo 8:")

amigos = ["williams", "thiago", "arcanjo", "xande", "vere", "chris", "serra"]

print([(lambda nome: nome.capitalize())(amigo) for amigo in amigos])

# Exemplo 9
print("Exemplo 9:")


print([numero * 3 for numero in range(1, 10)])

# Exemplo 10
print("Exemplo 10:")

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 11
print("Exemplo 11:")

print([str(numero) for numero in [1, 2, 3, 4, 5]])
