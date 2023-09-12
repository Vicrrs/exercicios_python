# Ordenacao de listas
def ordenar_selecao(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        
numeros = [64, 25, 12, 22, 11]
ordenar_selecao(numeros)
print(numeros)
