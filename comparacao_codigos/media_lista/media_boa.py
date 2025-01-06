# Código bom: calculando a média de uma lista de números

def calcular_media(numeros):
    if not numeros:
        raise ValueError("A lista de numeros nao pode estar vazia")
    return sum(numeros) / len(numeros)

numeros = [10, 20, 30, 40, 50]
try:
    print(calcular_media(numeros))
except ValueError as e:
    print(e)


"""
Uso de sum() para calcular a soma diretamente, mais eficiente e legível.

Nomes de variáveis e funções mais descritivos.

Tratamento de erro para listas vazias, evitando problemas durante a execução.
"""
