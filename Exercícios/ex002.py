def verifica(n1, n2):
    if n1 > n2:
        print("O n1 é maior que o n2!")
    else:
        print("O n2 é maior que o n1!")


if __name__ == "__main__":
    n1 = float(input("Digite o primeiro número :"))
    n2 = float(input("Digite o segundo número: "))
    verifica(n1, n2)
