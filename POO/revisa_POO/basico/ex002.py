#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Método em uma classe

"""
    Teoria: Adicionamos um método `cumprimentar` que retorna uma string formatada.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

pessoa1 = Pessoa("João", 30)
print(pessoa1.comprimentar()) # Olá, meu nome é João e tenho 30 anos.

