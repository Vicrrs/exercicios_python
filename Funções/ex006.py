def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


print(f"O fatorial de {6} é {fatorial(6)}")
