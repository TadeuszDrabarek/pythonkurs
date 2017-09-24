# -*- coding: utf-8 -*-
# To jest początek programu

import random

l=['a',2,3,4,5,6,7,8,9,10,'j','q','k']

sl={}   # tu będą karty jako klucz a liczba kart jako wartość (w talii są po 4 karty)
s2={}   # tu będą przechowywane karty wybrane przez użytkownika
s3={}   # tu będą indexy, numer danewgo elementu na liście wejściowej
wyb=[]     # tu będzie finalna lista wybranych kart, już uszeregowana

for (i,x) in enumerate(l):
    sl[str(x)]=4               # ustawiamy, że po 4 kart w talii, konwertujemy ew. liczby na string
    s2[str(x)]=0               # jeszcze nic nie wybrano
    s3[str(x)]=i               # tu zapisuję index danego elementu na liście l
    
while(True):
    inp=str(input('Podaj kartę z listy : ('+str(l)+')\n ! - oznacza wyjście, ENTER - losowanie randomowe :'))
    if ((inp in sl.keys()) and (sl[inp]>0)):             # czy jest taki klucz i jeżeli tak to czy są jeszcze takie elementy (>0)
        s2[inp]+=1           # dodajemy ten element do wybranych
        sl[inp]-=1           # usuwamy go z dostępnych
    elif (inp.upper() in ['!','E']):
        break
    elif (inp==""):
        while(True):
            ins=input('Ile kart wylosować ? :')
            if (ins.isdigit()):
                break
            print('Tylko cyfry 0-9')
        ile=int(ins)
        iii=0
        while (iii<ile):
            while(True):
                ll=random.randint(0,len(l)-1)
                los=str(l[ll])
                if (sl[los]>0):
                    break
            s2[los]+=1           # dodajemy ten element do wybranych
            sl[los]-=1           # usuwamy go z dostępnych   
            print('Wybrano:',los)
            iii+=1
    else:
        print('Podałeś kartę spoza zakresu')

wyn=[]                # to będzie lista wynikowa
for k in s2:                #przelatujemy po słowniku z elementami wybranymi przez użytkownika
    i=0
    while i<s2[k]:              #  kręcimy tyle razy ile razy dany element został wybrany
        wyn.append(l[s3[k]])    #  dodajemy do listy wynikowej ten element tyle razy, uwaga, dodajemy z listy oryginalnej a znajdujemy index pezez s3
        i+=1
        
print('Wybór po uszeregowaniu :',wyn)