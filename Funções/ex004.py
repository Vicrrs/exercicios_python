# Funções em Python podem retornar mais de um valor:
def quociente_resto(x, y):
    quociente = x // y
    resto = x % y
    return (quociente, resto)

print(f"Quociente e resoto: {quociente_resto(9, 4)}")
