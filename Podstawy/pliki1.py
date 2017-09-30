# -*- coding: utf-8 -*-
# To jest początek programu

import os 
import fnmatch
        
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
    print('D-dodawanie, P-printuj listę, T-test, W-zapis do pliku, R-czytaj polik, A-dopisz do pliku')
    print('L-ls, Z-list test, E-załaduj rekordy z pliku, Q-Wyjście')
    w=input(':')
    w=w.upper()
    if (w=='Q'):
        break
    elif (w=='Z'):
        print('CWD=',os.getcwd())
        for x in os.listdir():
            if fnmatch.fnmatch(x.upper(),'*.TXT'):
                print(x)        
    elif (w=='D'):
        print('Podaj imię, nazwisko, stanowisko i pensję:')
        imie=input('Imię:')
        nazwisko=input('Nazwisko:')
        stanowisko=input('Stanowisko:')
        pensja=float(input('Pensja (podaj liczbę dziesiętną):'))
        pracownik=Pracownik(imie,nazwisko,stanowisko,pensja)
        L.append(pracownik)
    elif (w=='P'):
        for i in L:
            print(i)
    elif (w=='T'):
        x=Pracownik('','','',0)
        x.info(L)
    elif (w=='W'):
        print('CWD=',os.getcwd())
        nazwa=input('Podaj nazwę pliku:')
        F=open(nazwa,'w')
        for i in L:
            F.write(str(i)+'\n')
        F.close()
        print('Zapisane!')
    elif (w=='A'):
        print('CWD=',os.getcwd())
        nazwa=input('Podaj nazwę pliku:')
        F=open(nazwa,'a')
        for i in L:
            F.write(str(i)+'\n')
        F.close()
        print('Zapisane!'    )
    elif (w=='R'):
        print('CWD=',os.getcwd())
        nazwa=input('Podaj nazwę pliku:')
        F=open(nazwa,'r')
        lines=F.readlines()
        F.close()
        for j,i in enumerate(lines):
            #print(('%4i - >%s')%(j,str(i)), end="")
            print(j,i.split('|'))
        print('Koniec!')
    elif (w=='E'):
        print('CWD=',os.getcwd())
        nazwa=input('Podaj nazwę pliku:')
        F=open(nazwa,'r')
        lines=F.readlines()
        F.close()
        for i,l in enumerate(lines):
            h=l.split('|')
            imie=h[0].strip()
            nazwisko=h[1].strip()
            stanowisko=h[2].strip()
            pensja=h[3].strip()
            print(imie,nazwisko,stanowisko,pensja)
            pracownik=Pracownik(imie,nazwisko,stanowisko,float(pensja))
            L.append(pracownik)            
        print('Koniec!'    )
    elif (w=='L'):
        print('CWD=',os.getcwd())
        print(os.listdir())
    
        '''
        
        '''
        
