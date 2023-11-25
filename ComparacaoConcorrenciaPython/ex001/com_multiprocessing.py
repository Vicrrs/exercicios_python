from multiprocessing import Pool
import time

def calcular_soma(numeros):
    return sum(numeros)


if __name__ == "__main__":
    numeros = range(1_000_000_000)

    inicio = time.time()

    with Pool(processes=4) as pool:
        resultados = pool.map(calcular_soma, [numeros[i::4] for i in range(4)])
    resultado_final = sum(resultados)

    fim = time.time()

    tempo_execucao = fim - inicio

    print(resultado_final)
    print(f"Tempo de execução: {tempo_execucao} segundos")
