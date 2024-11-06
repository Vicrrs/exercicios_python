# Cada numero de 0 ate n-1 é somado com cada numero de 0 ate n-1
# operacao n * n
# O(n^2) -> Crescimento quadrático
def soma(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += i + j
    return soma

print(soma(5))
