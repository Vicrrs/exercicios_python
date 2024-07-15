#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Getters e Setters

"""
    Teoria: Usamos propriedades para criar métodos getters e setters para controlar o acesso aos 
    atributos privados.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

pessoa1 = Pessoa("João", 30)
print(pessoa1.nome) # João
pessoa1.nome = "Carlos"
print(pessoa1.nome) # Carlos

