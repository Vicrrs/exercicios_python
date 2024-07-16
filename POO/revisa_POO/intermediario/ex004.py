#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Polimorfismo

"""
    Teoria: A funcao `emitir som` pode aceitar qualquer objeto que tenha um método `fazer_som`, demonstrando
    polimorfismo.
"""

class Ave:
    def fazer_som(self):
        return "piu piu"

class Galinha(Ave):
    def fazer_som(self):
        return "Cocoricó"

def emitir_som(ave):
    print(ave.fazer_som())

ave = Ave()
galinha = Galinha()
emitir_som(ave)
emitir_som(galinha)

