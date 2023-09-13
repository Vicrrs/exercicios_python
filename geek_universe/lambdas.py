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
