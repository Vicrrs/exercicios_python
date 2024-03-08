# Gerando uma sequÊncia de números

def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1
        
for numero in contador(5):
    print(numero)
        