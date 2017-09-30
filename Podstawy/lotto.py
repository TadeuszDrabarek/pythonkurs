# -*- coding: utf-8 -*-
# To jest początek programu

import random


class Lotto:
    def __init__(self):
        self.L=set()
    def losowanie(self):
        while(True):
            i=random.randint(1,49)
            if (len(self.L)==6):
                break
            self.L.add(i)
    def podaj(self):
        self.L=set()
        while(True):
            if (len(self.L)==6):
                break            
            while(True):
                i=input('Podaj liczbę ['+str(len(self.L)+1)+'] 1-49 :')
                if (i.isdigit()):
                    i=int(i)
                    if ((i>=0) and (i<=49)):
                        break
            self.L.add(i)    
    def __str__(self):
        return str(self.L)
    
    def sort(self):
        return sorted(self.L)
    
    def sprawdz(self,test):
        return (self.L&test.L)

L=Lotto()
L.losowanie()
print('Losowanie:',L.sort())

moje=Lotto()
moje.podaj()
print('moje      :',moje.sort())

print('Wygrana ? :',L.sprawdz(moje))