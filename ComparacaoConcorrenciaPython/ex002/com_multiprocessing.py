import time
from multiprocessing import Pool

def soma_dos_quadrados(numeros):
    return sum(x**2 for x in numeros)

if __name__ == "__main__":
    numeros = range(1, 100_000_001)

    inicio = time.time()

    with Pool(4) as pool:
        partes = [numeros[i::4] for i in range(4)]
        resultados = pool.map(soma_dos_quadrados, partes)
    resultado_final = sum(resultados)

    fim = time.time()

    tempo_execucao = fim - inicio

    print(f"Soma dos quadrados (Multiprocessing): {resultado_final}")
    print(f"Tempo de execução: {tempo_execucao} segundos")
