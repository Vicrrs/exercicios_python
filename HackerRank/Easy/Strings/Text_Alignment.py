""" Task:
    Em Python, uma sequência de texto pode ser alinhada à esquerda, à direita e ao centro.

    .ljust(largura)

    Este método retorna uma sequência alinhada à esquerda de comprimento width.

    >>> width = 20
    >>> print 'HackerRank'.ljust(largura,'-')
    HackerRank----------

    .center(largura)

    Este método retorna uma sequência centralizada de comprimento width.

    >>> width = 20
    >>> print 'HackerRank'.center(largura,'-')
    -----HackerRank-----

    .rjust(largura)

    Este método retorna uma sequência alinhada à direita de comprimento width.

    >>> width = 20
    >>> print 'HackerRank'.rjust(largura,'-')
    ----------HackerRank

    Tarefa

    Você recebe um código parcial que é usado para gerar o logotipo do HackerRank de espessura variável.
    Sua tarefa é substituir o espaço em branco (______) por rjust, ljust ou center.

    Formato de entrada

    Uma única linha contendo o valor de espessura do logotipo.

    Restrições

    A espessura deve ser um número ímpar.

    0 < espessura < 50

    Formato de saída

    Produza o logotipo desejado.

    Entrada de amostra

    5

    Saída de amostra
    
    Divisao da LOGO:
    1. Cone Superior: Um formato de pirâmide que cresce em largura, começando do topo até alcançar a espessura máxima.
    2. Pilares Superiores: Duas barras verticais, uma ao lado da outra, com um espaço entre elas.
    3. Cinturao central: Uma barra horizontal longa que conecta os pilares.
    4. Pilares inferiores: Esta parte espelha os pilares superiores.
    5. Cone Inferior: Esta parte espelha o cone superior, mas de forma invertida.
"""

print("Resolvendo o Problema")

thickness = int(input())  # This must be an odd number
c = 'H'
    
# Cone Superior
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    
# Pilares Superiores
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
# Cinturão Central
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))    
    
# Pilares Inferiores
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))    
    
# Cone Inferior
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))  


