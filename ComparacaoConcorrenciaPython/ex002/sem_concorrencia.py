import time

def soma_dos_quadrados(numeros):
    return sum(x ** 2 for x in numeros)


numeros = range(1, 100_000_001)

inicio = time.time()

resultado = soma_dos_quadrados(numeros)

fim = time.time()

tempo_exec = fim - inicio

print(f"Soma dos quadrados (Sequencial): {resultado}")
print(f"Tempo de execução: {tempo_exec} segundos")

