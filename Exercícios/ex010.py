# geradores são usados para criar sequências de itens de forma eficiente
# yield permite criar geradores que não ocupam muita memória
def gerar_pares():
    n = 0
    while True:
        yield n
        n += 2
        
pares = gerar_pares()
for _ in range(5):
    print(next(pares))
