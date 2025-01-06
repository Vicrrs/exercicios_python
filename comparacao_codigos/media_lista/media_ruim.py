# Código ruim: calculando a média de uma lista de números

def calc_media(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    m = s / len(lista)
    return m

nums = [10, 20, 30, 40, 50]
print(calc_media(nums))
