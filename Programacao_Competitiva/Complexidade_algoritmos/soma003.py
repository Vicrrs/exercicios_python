# Complexidade de espaço
# Esse algoritmo recebe numero n e retorna a soma de todos os numeros de 0 ate n-1,
# usandouma lista para armazenar os numero
# O(n) -> Crescimento linear, pois ele ocupa n posicoes na memoria, uma para cada numero de 0 ate n-1
def soma(n):
    numeros = [i for i in range(n)]
    soma = 0
    for i in numeros:
        soma += 1
    return soma

print(soma(5))