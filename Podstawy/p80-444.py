# -*- coding: utf-8 -*-
# To jest początek programu

class rgb:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
    def __add__(self,other):
        return rgb((self.r+other.r)//2,(self.g+other.g)//2,(self.b+other.b)//2)
    def __str__(self):
        return '[%3i,%3i,%3i]'%(self.r,self.g,self.b)
    

a=rgb(0,0,0)
b=rgb(255,255,255)

print('a=',a)
print('b=',b)
print('a+b=',a+b+b)
