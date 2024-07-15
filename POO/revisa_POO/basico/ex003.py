#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Atributos publicos e privados

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome # Atributo privado
        self.idade = idade # Atributo publico

pessoa1 = Pessoa("João", 30)
print(pessoa1.idade) # 30
# print(pessoa1._nome) # Não é recomendado acessar diretamente.

