#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definindo uma classe e criando um objeto

"""
    Teoria: Aqui definimos uma classe `Pessoa` com um construtor (__init__) que inicializa os atributos
    `nome` e `idade`. Criamos um objeto `pessoa1` da classe `Pessoa`.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)
print(pessoa1.idade)

