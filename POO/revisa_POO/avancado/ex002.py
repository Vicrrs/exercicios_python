#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Métodos e Atributos de Instância vs. de Classe

"""
    Teoria: `aumento` é um atributo de classe compartilhado entre todas as instancias, enquanto
    `nome` e `salario` são atributos de instancia unicos de cada objeto.
"""

class Funcionario:
    aumento = 1.05  # Atributo de classe

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_aumento(self):
        self.salario *= Funcionario.aumento

funcionario1 = Funcionario("Alice", 5000)
funcionario2 = Funcionario("Bob", 6000)

funcionario1.aplicar_aumento()
print(funcionario1.salario)  # 5250.0
print(funcionario2.salario)  # 6000.0


