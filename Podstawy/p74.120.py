# -*- coding: utf-8 -*-
# To jest początek programu

def dodaj(x):
    w=0
    for i in x:
        w+=i
    return w

def odejmij(x):
    w=x[0]
    i=1
    while(i<len(x)):
        w-=x[i]
        i+=1
    return w  

def potega(x):
    w=x[0]
    i=1
    while(i<x[1]):
        w*=x[0]
        i+=1
    return w

def frange(x):
    l=[]
    if (((x[0]<x[1]) and (x[2]>0)) or ((x[0]>x[1]) and (x[2]<0))):
        i=x[0]
        while(i<=x[1]):
            l.append(i)
            i+=x[2]
    return l
        
def zapytaj(i=2):
    w=[]
    while(True):
        while(True):
            a=str(input('Podaj liczbę ('+str(len(w)+1)+') :'))
            if (a.isdigit()):
                w.append(int(a))
                break
        if (len(w)==i):
            break      
    return w

def kelwiny(x):
    w=[]
    for i in x:
        w.append(i+273.15)
    return w

def zapytaj3(j):
    i=len(j)
    w=[]
    k=0
    while(True):
        a=str(input('Podaj liczbę ('+str(j[k])+') :'))
        w.append(float(a))
        k+=1
        if (len(w)==i):
            break      
    return w

def tabelka(a,b):
    i=len(a)
    j=len(b)
    k=i if i<j else j
    l=0
    print('|%7s|%-7s|'% ( 'C','K'))
    print('-'*17)
    while(l<k):
        print('|%7.2f|%-7.2f|'% (a[l],b[l]))
        l+=1

    
while(True):
    print('O-odejmowanie, D-dodwanie, P-potegowanie, F-range, W-wyjście');
    s=input('Co chcesz zrobić :')
    if (s.upper()=='D'):
        ab=zapytaj(2)
        #print(ab)
        print(dodaj(ab))
    if (s.upper()=='O'):
        ab=zapytaj(2)
        #print(ab)
        print(odejmij(ab))
    if (s.upper()=='P'):
        ab=zapytaj(2)
    if (s.upper()=='F'):
        ab=zapytaj3(['Min','Max','Krok'])
        c=frange(ab)
        k=kelwiny(c)
        tabelka(c,k)
    if (s.upper()=='W'):
        break
        
    