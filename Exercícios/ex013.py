# Arvores Binarias
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    else:
        if valor <= raiz.valor:
            raiz.esquerda = inserir(raiz.esquerda, valor)
        else:
            raiz.direita = inserir(raiz.direita, valor)
    return raiz

def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.valor, end=' ')
        em_ordem(raiz.direita)

raiz = None
raiz = inserir(raiz, 50)
raiz = inserir(raiz, 30)
raiz = inserir(raiz, 70)
raiz = inserir(raiz, 20)
raiz = inserir(raiz, 40)
em_ordem(raiz)  # Saída: 20 30 40 50 70
