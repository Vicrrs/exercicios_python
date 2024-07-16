#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Encapsulamento com Propriedades

"""
    Teoria: Utilizarmos propriedades para encapsular o acesso ao atributo `saldo`, permitindo validação
    ao modificar o saldo.
"""

class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

conta = ContaBancaria(100)
print(conta.saldo) # 100
conta.saldo = 200
print(conta.saldo) # 200

