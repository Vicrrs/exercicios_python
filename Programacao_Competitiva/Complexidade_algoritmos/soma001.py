# Retorna a soma de todos os numeros comecando de azero ate n-1
# O(n) -> Crescimento Linear, pois ele executa n operacoes uma para cada numero
def soma(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

print(soma(5))
