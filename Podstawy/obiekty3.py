# -*- coding: utf-8 -*-
# To jest początek programu

class Compare:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return '[%i,%i]' % (self.x,self.y)
    def __add__(self,other):
        return(Compare(self.x+other.x,self.y+other.y))
    def __sub__(self,other):
        return(Compare(self.x-other.x,self.y-other.y))    
    def __eq__(self,other):
        return ((self.x==other.x) and (self.y==other.y)) 
    def __gt__(self,other):
        return ((self.x**2+self.y**2)>(other.x**2+other.y**2)) 
    def __neg__(self):
        return (Compare(-self.x,-self.y))
    
p1=Compare(5,6)
print(p1)

p2=Compare(11,1)
print(p2)

p3=p1+p2
p4=p1-p2
p5=p2-p1

print(p3)
print(p4)
print(p5)
print('p4==p5',p4==p5)
print('p5==p4',p5==p4)

print('p5>p4',p1>p2)
print('p4>p5',p2>p1)

print('p3',p3)
print('-p3',-p3)

print('p3+(-p3)',p3+(-p3))