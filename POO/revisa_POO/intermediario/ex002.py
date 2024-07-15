#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Herança Múltipla

"""
    Teoria: `Onitorrinco` herda de `Mamifero` e `Ave`, combinando funcionalidades de ambas as classes.
"""

class Mamifero:
    def amamentar(self):
        return "Amamentando..."

class Ave:
    def botar_ovo(self):
        return "Botando ovo..."

class Onintorrinco(Mamifero, Ave):
    pass

onintorrinco = Onintorrinco()
print(onintorrinco.amamentar()) # Amamentando...
print(onintorrinco.botar_ovo()) # botando ovo...

