# usamos uma matriz para armazenar os números, cada linha da matriz é um vetor de 0 até n - 1, 
# estamos consumindo mais memória e tendo o mesmo resultado
# O(n^2) -> complexidade Quadrática de espaço, pois ele ocupa n * n posições na memória, cada número de 0 até n - 1 é armazenado n - 1 vezes
def soma(n):
    numeros = [[i for i in range(n)] for j in range(n)]
    soma = 0
    for i in numeros[0]:
        soma += 1
    return soma

print(soma(10))
