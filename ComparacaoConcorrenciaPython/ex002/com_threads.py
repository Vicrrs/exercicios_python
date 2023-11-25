from threading import Thread
import time

def soma_dos_quadrados(numeros, resultado):
    resultado.append(sum(x**2 for x in numeros))

if __name__ == "__main__":
    numeros = range(1, 100_000_001)
    resultados = []
    threads = []

    inicio = time.time()

    for i in range(4):
        parte = numeros[i::4]
        thread = Thread(target=soma_dos_quadrados, args=(parte, resultados))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    fim = time.time()
    tempo_execucao = fim - inicio

    resultado_final = sum(resultados)
    print(f"Soma dos quadrados (Threads): {resultado_final}")
    print(f"Tempo de execução: {tempo_execucao} segundos")

