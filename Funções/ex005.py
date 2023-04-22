def eleva_ao_quadrado(n):
    return n ** 2


print(list(map(eleva_ao_quadrado, range(5))))

print(list(map(lambda x: x ** 2, range(5))))
