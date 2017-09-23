# -*- coding: utf-8 -*-
# To jest początek programu
import random

wylosowane=set()  
ile=6;

while (len(wylosowane)<ile):
    liczba=random.randint(1,49)
    wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
else:
    print(wylosowane)

lista=[1,4,8,4,1,3,6,7,4,1,7,4]
i=0
while (i<len(lista)):
    print("Element "+str(i)+'-ty ma wartość :'+str(lista[i]))
    i+=1

lista=[]    
print("Wpisuj kolejne wartości do listy, jeżeli chcesz zakończyć to wpisz Q!")

flaga=True
while (flaga):
    t=input("Podaj "+str(len(lista)+1)+"-tą wartość :")
    if (t.upper()!='Q!'):
        lista.append(t)
    else:
        flaga=False
    
print('Wpisałeś :')
i=0
while(i<len(lista)):
    print(lista[i])
    i+=1
    
    
for a in lista:
    print(a)
    

