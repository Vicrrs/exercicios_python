# a, b =  input().split()

# print(a)
# print(b)
try:
    # Solicitando a entrada do usuario
    entrada = input("Digite os dois valores separados por espaço: ")
    a, b = entrada.split()

    # Imprime os valores separados
    print(f"Primeiro valor: {a}")
    print(f"Segundo valor: {b}")
except ValueError:
    print("ERRO, digite o valor separado por espaço")