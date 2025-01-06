# Código ruim: Verificando se um numero é primo

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = 7
print(eh_primo(num))
