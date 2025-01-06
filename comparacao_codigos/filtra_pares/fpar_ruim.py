# Código ruim: filtro de numeros pares

def filtrar_pares(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_pares(numeros))
