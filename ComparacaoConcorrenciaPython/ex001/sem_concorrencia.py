import time

def calcular_soma(numeros):
    return sum(numeros)

numeros = range(1_000_000_000)

inicio = time.time()

resultado = calcular_soma(numeros)

fim = time.time()
tempo_execucao = fim - inicio

print(resultado)
print(f"Tempo de execução: {tempo_execucao} segundos")
