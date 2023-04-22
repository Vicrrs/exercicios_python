def verifica(num):
    resultado = print("O número é positivo" if num > 0 else "O número é negativo." if num < 0 else "O número é zero")
    return resultado


if __name__ == "__main__":
    num = int(input("Digite um número inteiro: "))
    verifica(num)