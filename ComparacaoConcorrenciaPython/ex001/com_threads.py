from threading import Thread
import time

def calcular_soma(numeros, resultado):
    resultado.append(sum(numeros))

if __name__ == "__main__":
    numeros = range(1_000_000_000)
    resultados = []
    threads = []

    # Registrar o tempo antes da execução
    inicio = time.time()

    for i in range(4):
        thread = Thread(target=calcular_soma, args=(numeros[i::4], resultados))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    resultado_final = sum(resultados)

    # Registrar o tempo após a execução
    fim = time.time()

    # Calcular o tempo de execução
    tempo_execucao = fim - inicio

    print(resultado_final)
    print(f"Tempo de execução: {tempo_execucao} segundos")
