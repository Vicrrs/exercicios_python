#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sobrescrita de Método

"""
    Teoria: `carro` sobrescreve o método `mover` de `Veiculo` para fornecer uma implementação específica.
"""

class Veiculo:
    def mover(self):
        return "O veiculo esta sem movendo"

class Carro(Veiculo):
    def mover(self):
        return "O carro esta se movendo"

veiculo = Veiculo()
carro = Carro()

print(veiculo.mover()) # O veiculo esta se movendo
print(carro.mover()) # O carro esta se movendo

