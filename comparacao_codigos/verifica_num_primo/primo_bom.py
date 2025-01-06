# Código bom: Verificando se um número é primo

import math

def verificar_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, math.isqrt(numero) + 1, 2):
        if numero % i == 0:
            return False
    return True

numero = 7
print(verificar_primo(numero))
