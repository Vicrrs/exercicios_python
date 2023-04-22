# Percorrendo intervalos em Python, intervalo começam com 0
for i in range(10):
    print(i)
    if i == 7:
        for j in range(10, 20):
            print(j)
        break
