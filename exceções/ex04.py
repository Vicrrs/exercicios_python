try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Digite um número válido")
else:
    print("O número digitado foi: ", x)