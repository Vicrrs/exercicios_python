# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    try:
        x = input().strip()
        if x == "esquerda":
            print("ingles")
        elif x == "direita":
            print("frances")
        elif x == "nenhuma":
            print("portugues")
        elif x == "as duas":
            print("caiu")
    except EOFError:
        break