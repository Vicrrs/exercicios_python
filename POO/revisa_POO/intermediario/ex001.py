#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Herança simples

"""
    Teoria: `Cachorro` herda de `Animal` e implementa o método abstrato `fazer_som`.
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError

class Cachorro(Animal):
    def fazer_som(self):
        return "AU AU!"

cachorro = Cachorro("Rex")
print(cachorro.nome) # Rex
print(cachorro.fazer_som()) # Au Au!

