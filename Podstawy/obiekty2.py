# -*- coding: utf-8 -*-
# To jest początek programu

        
class Pracownik:
    imie=''
    nazwisko=''
    stanowisko=''
    pensja=0
    def __init__(self,imie,nazwisko,stanowisko='stażysta',pensja=1000):
        self.imie=imie
        self.nazwisko=nazwisko
        self.stanowisko=stanowisko
        self.pensja=pensja
        
    def __str__(self):
        return ('%-15s|%-15s|%-20s|%8.2f' % (self.imie, self.nazwisko, self.stanowisko, self.pensja)) 
    def info(self, L):
        for v in L:
            print(v)
        
        
L=[]
while(True):
    w=input('D-dodawanie, P-printuj listę, T-test, Q-Wyjście :')
    w=w.upper()
    if (w=='Q'):
        break
    elif (w=='D'):
        print('Podaj imię, nazwisko, stanowisko i pensję:')
        imie=input('Imię:')
        nazwisko=input('Nazwisko:')
        stanowisko=input('Stanowisko:')
        pensja=int(input('Pensja (podaj liczbę dziesiętną):'))
        pracownik=Pracownik(imie,nazwisko,stanowisko,pensja)
        L.append(pracownik)
    elif (w=='P'):
        for i in L:
            print(i)
    elif (w=='T'):
        x=Pracownik('','','',0)
        x.info(L)
        
