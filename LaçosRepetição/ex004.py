elemento = 10
esta_presente = False

lista = [1, 2, 3, 20, 5, 10, 9, 50, 54, 23]
for item in lista:
    if item == elemento:
        esta_presente = True

if esta_presente:
    print("Elemento está na lista!")
else:
    print("Elemento não está na lista!")
