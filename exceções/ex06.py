try:
    x = int(input("Digite um número: "))
    assert x > 0, "O número dever ser positivo!"
except (ValueError, AssertionError) as e:
    print("Ocorreu um erro: ", e)
else:
    print("O número digitado foi: ", x)