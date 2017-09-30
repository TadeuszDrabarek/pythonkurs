# -*- coding: utf-8 -*-
# To jest początek programu

# COŚ TU NIE GRA ZA BARDZO ...

import random

class A:
    def __init__(self,kolor):
        self.kolor=kolor
        print('Jestem A koloru',kolor)

class Bazowa:
    def __init__(self):
        self.a=1
        print("Jestem BAZOWA")
    def info(self):
        print('Info BAZOWA')
        
class Potomna(Bazowa,A):
    def __init__(self,kolor):
        super(Bazowa).__init__()
        super(A).__init__(str, kolor)
        print("Jestem POTOMNA")
    def info(self):
        super().info()
        print('Info POTOMNA') 
        print('Mój kolor :',super(A).kolor)
        
a=Potomna('zielony')
a.info()
print(a.a)