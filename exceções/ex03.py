try:
    x = int(input("Digite um número: "))
    print("O número digitado foi: ", x)
    y = 1 / x
except ValueError:
    print("Digite um número válido")
except ZeroDivisionError:
    print("Não é possível dividir por zero")