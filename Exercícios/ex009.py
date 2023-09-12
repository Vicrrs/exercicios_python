def calcular_media(lista):
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia!")
    
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"A média dos numeros é {media}")
    