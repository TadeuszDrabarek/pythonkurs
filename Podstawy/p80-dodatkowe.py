# -*- coding: utf-8 -*-
# To jest początek programu

class Kontrakt:    
    def __init__(self,nazwa,kwota):
        self.nazwa=nazwa
        self.pensja=1000.00 if (nazwa=='staż') else kwota
    def pensja(self):
        return self.pensja
    def stanowisko(self):
        return self.nazwa  
        
        
class Pracownik(Kontrakt):
    def __init__(self,imie, nazwisko, kwota=1000.00, nazwa='staż'):
        super().__init__(nazwa,kwota)
        self.imie=imie
        self.nazwisko=nazwisko
    def pensja():
        return super().pensja();
    def zmien_kontrakt(self, nazwa, kwota):
        super().__init__(nazwa,kwota)
    def wypisz_kontrakt(self):
        print('Pracownik: %s %s, kontrakt: %s, pensja: %8.2f PLN'%(self.imie, self.nazwisko,self.nazwa,self.pensja))
    def __str__(self):
        return (' %20s|%20s|%10s|%8.2fPLN'%(self.imie, self.nazwisko,self.nazwa,self.pensja))
        
        
class Firma:
    def __init__(self):
        self.L=[]
        while (True):
            w=input('A-dodaj, D-usuń, P-print, Q-wyjście :').upper()
            if (w=='Q'):
                print('Bye, see you next time...')
                break;
            if (w=='D'):
                index=int(input('Kogo usunąć :'))-1
                kogo=self.L.pop(index)
            if (w=='A'):
                i=input('Imię :')
                j=input('Nazwisko :')
                s=input('Stanowisko :')
                if (s!='staż'):
                    k=float(input('Kwota :'))
                else:
                    k=0
                a=Pracownik(i,j,k,s)
                self.dodaj_pracownika(a)
            if (w=='P'):
                self.wypisz();            
        return
    def dodaj_pracownika(self,a):
        self.L.append(a)
    def wypisz(self,):
        print('%3s| %20s|%20s|%10s|%8s'%('Lp.' ,'Imię','Nazwisko','Stanowisko','Pensja'))
        print('-'*70)
        for i,k in enumerate(self.L):
            print('%3i|%s'%(i+1,k))
    
'''
a=Pracownik('Ambrozy','Kleks')
a.wypisz_kontrakt()

b=Pracownik('Alama','Kota',2000,'etat')
b.wypisz_kontrakt()

c=Pracownik('Bleble','aaaas',3000,'etat')
c.wypisz_kontrakt()


f=Firma()
f.dodaj_pracownika(a)
f.dodaj_pracownika(b)
f.dodaj_pracownika(c)

f.wypisz();
'''

f=Firma()