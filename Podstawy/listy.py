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
    
print('Print 1 :')
for a in lista:
    print(a)
    
print('Print 2 :')
l=lista
for a in l:
    print(a)
   
print('Print 3 :')    
for j, a in enumerate(l):
    if (len(l)>0):
        if (j==0):
            print('{'+str(a)+', ', end='')
        elif (j<len(l)-1):
            print(str(a)+", ", end='')
        else:
            print(str(a)+'}')
    else:
        print('{'+str(a)+'}')
        

rc={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
for k in rc:
    print(k,rc[k])

# lista=[1,2,3,4]
# zbiór=set([1,2,3,4])
# słownik={a:b, ....}

lista=[1,2,3,4]
zbior=set([1,2,3,4])
zbior2={5,6,7,8,9}
slownik={'a':'aa', 'b':'bb'}

print(lista)
print(zbior)
print(zbior2)
print(slownik)

v=range(-10,20,1)
for a in v:
    print(a, end=' ')