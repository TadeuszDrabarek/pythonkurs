# -*- coding: utf-8 -*-
# To jest początek programu

def dodawanie(a,b):
    wynik=a+b
    return wynik
    
    
print(dodawanie(4,6))
    
    
def ijk():
    return {1,2,3,4,5,5,5,1}

l=ijk()
print(l)

def baza(imie, nazwisko, wiek, imie2='b/d', fajowy=False):
    rekord=[]
    rekord.append(imie.capitalize())
    rekord.append(imie2.capitalize())
    rekord.append(nazwisko.capitalize())
    rekord.append(wiek)
    rekord.append(fajowy)
    rekord.append('Kobieta' if (imie[len(imie)-1]=='a') else 'Mężczyzna')
    return(rekord)

print(baza(imie='Janina',imie2='Maria',nazwisko='Rokita',wiek=14,fajowy=True))
    
    
