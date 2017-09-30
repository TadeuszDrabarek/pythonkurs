# -*- coding: utf-8 -*-
# To jest początek programu

class zawodnik:
    def __init__(self,waga,wzrost):
        self.waga=waga
        self.wzrost=wzrost
    def bmi(self):
        return (self.waga/self.wzrost**2)

    
class zawodnicy:
    L=[]
    def __init__(self):
        return
    def add(self,Z):
        self.L.append(Z)
    def sort(self):
        return sorted(self.L)
    
Z1=zawodnik(75,1.74)
Z2=zawodnik(80,1.84)
Z3=zawodnik(85,1.94)
Z4=zawodnik(70,2.04)

print('BMI=',round(Z1.bmi(),2))
print('BMI=',round(Z2.bmi(),2))
print('BMI=',round(Z3.bmi(),2))
print('BMI=',round(Z4.bmi(),2))

ZZ=zawodnicy()

ZZ.add(Z1.bmi())
ZZ.add(Z2.bmi())
ZZ.add(Z3.bmi())
ZZ.add(Z4.bmi())



print(ZZ.sort())