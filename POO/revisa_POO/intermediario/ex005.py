#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Classes abstratas

"""
    Teoria: `Animal` é uma classe abstrata que define um método abstrato `fazer_som`, que deve ser implementado pelas
    subclasses.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "AU AU"

cachorro = Cachorro()
print(cachorro.fazer_som())

