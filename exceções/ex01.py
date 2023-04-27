try:
    x = int(input("Digite um número: "))
    y = 1 / x
except (ValueError, ZeroDivisionError) as e:
    print("Ocorreu um erro:", e)
else:
    print("O resultado da inversa é:", y)
