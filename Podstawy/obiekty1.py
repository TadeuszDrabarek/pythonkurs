# -*- coding: utf-8 -*-
# To jest początek programu

class Testowa:  

    
    def __init__(self,zmienna1,zmienna2):
        print('Jestem w konstruktorze')
        self.zmienna1=zmienna1
        self.zmienna2=zmienna2
        
    def info(self):
        print(self.zmienna1,self.zmienna2)
        
    def dodaj(self,i):
        self.zmienna1+=i
        
        
o1=Testowa(5,'A')

o1.info()
o1.dodaj(5)

o2=Testowa(3,'B')

o1.info()
o2.info()

aaa=19

print(aaa.__str__())