# -*- coding: utf-8 -*-
# To jest początek programu

class Produkt:
    def __init__(self,nazwa,cena):
        self.nazwa=nazwa
        self.cena=cena
    def print(self):
        print('Nazwa :%15s ---- %8.2f PLN'%(self.nazwa, self.cena))
    def __str__(self):
        return ('Nazwa :%15s ---- %8.2f PLN'%(self.nazwa, self.cena))        
        
class Oprogramowanie(Produkt):
    ile=0;
    def __init__(self,nazwa,cena,jezyk,system):
        super().__init__(nazwa,cena)
        self.jezyk=jezyk
        self.system=system
        Oprogramowanie.ile=Oprogramowanie.ile+1
    def print(self):
        super().print()
        print('Język :%15s, system :%15s'%(self.jezyk,self.system))
    def __str__(self):
        return ('%s, język :%15s, system :%15s'%(super().__str__(),self.jezyk,self.system))
        
class Szkolenia(Oprogramowanie):
    ile=0
    def __init__(self,nazwa,cena,jezyk,system,termin):
        super().__init__(nazwa,cena,jezyk,system)
        self.termin=termin
        Szkolenia.ile+=1
        Oprogramowanie.ile-=1
    def print(self):
        super().print()
        print('Termin :%s'%(self.termin))
    def __str__(self):
        return ('%s, termin :%s'% (super().__str__(),self.termin))
        
        

class Testowa:
    def __init__(self):
        while (True):
            w=input('Co testujemy (0-Wyjście, 1-Oprogramowanie, 2-Szkolenia) :')
            if (w=='0'):
                break
            elif (w=='1'):
                op=Oprogramowanie('Python 4',159.99,'PYTHON','MAC OS 12')
                print(op)
                print('Ile razy :%i'%op.ile)
            elif (w=='2'):
                op=Szkolenia('Java 4',259.99,'PHP','MS DOS 5.1','1997-10-01')
                print(op)            
                print('Ile razy :%i'%op.ile)

a=Testowa()