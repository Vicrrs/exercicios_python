"""
Utilizando lambdas

São funcoes sem nome, ou seja, funcoes anonimas.
"""
# Funcao em python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressao lambda
lambda x: 3 * x + 1

# Usando expressao lambda
calc = lambda x: 3 * x + 1

print(calc(4))

print("-=-"*10)

# Podemos ter expressoes com multiplas entradas
nome_completo = lambda nome, sobre_nome: nome.strip().title() + ' ' + sobre_nome.strip().title()

print(nome_completo("VICTOR   ", "    roza"))

# Nenhuma ou varias entradas com lamda
# nenhuma
love = lambda : "Como nao amar python?"

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1/ x+1/y+1/z)

# n =lambda x1, x2, ..., xn: <expressao>

print(love())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


# Lista de autores
autores = ["Isaac Asimov", "Eduardo Spohr", "Douglas Adams", "Stephen Hawking", "Cólin Stuart", "J. J. Tolkien",
           "Carl Sagan"]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Funcoes Quadraticas
#f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna f(x)=a*x**2+b*x+c"""
    return lambda x: a*x**2+b*x+c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(1))
print(teste(2))
print(teste(3))

print(geradora_funcao_quadratica(3, 0, 1)(2))
