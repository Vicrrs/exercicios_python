#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Métodos de Classe e Métodos Estáticos

"""
    Teoria: Métodos de classe (`@classmethod`) podem acessar e modificar o estado da classe.
    Métodos estáticos (`@staticmethod`) não dependem do estado da classe ou instância.
"""

class Pessoa:
    populacao = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    @classmethod
    def obter_populacao(cls):
        return cls.populacao

    @staticmethod
    def saudacao():
        return "Ola!"

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

print(Pessoa.obter_populacao()) # 2
print(Pessoa.saudacao())

