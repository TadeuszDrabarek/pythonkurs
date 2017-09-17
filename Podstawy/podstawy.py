# -*- coding: utf-8 -*-

a="a";
b="napis";
c=7;
d=True;
e=False;

print(d);

print('To jest test');
print(a,b,c);

f=c+3;

print ("Wynik dodawanie =",f);

print(type(d));

# komentarz

""" 
sdfwsfasdfas to jest komentarz wieloliniowy

"""

print(5,True)
del(d)

d=4+f

print(d)



napis="to jest napis"

print(napis[5]);

print(napis.capitalize());

print(napis.encode('utf-8'));


lista=[1,2,"Ala","ma","kota",3.1415926,False,2+3j,None];
print(lista)
print(lista[5])
lista.append("nowy element tekstowy")
print(lista[1:6])

print(lista[:2])
print(lista[7:])

l1=[1,2,3,4]
l2=[7,8,9]
ll=[l1,l2]

print(ll);

print(ll[0][1])

# wielokrotnosc listy
print(l2)
l2 *= 3
print(l2)

print(len(l2))

del(l1[2])
print(l1)
l1.insert(1,'Wstawianie')
print(l1)

lista=[0,1,2,3,4,5,6,7,8,9]
print(lista[2:4])

napis='Jakis napis'
l=list(napis)
#print(list(napis)));
l.reverse();    

print(l);

num=[18,3,67,2,1,3,5]

num.sort();
print(num)



#mamy liste 3 produktów (cheleb, mleko, cukierki)
lista=['chleb','mleko','cukierki']
ceny=[3.15,10,20]

'''
ich=float(input('ile chleba :'));
im=float(input('ile mleka :'));
ic=float(input('ile cuierków :'));
ilosci=[ich,im,ic]

dz=ceny[0]*ilosci[0] + ceny[1]*ilosci[1]+ ceny[2]*ilosci[2]

'''

# print('do zapłaty ='+str(round(dz,2))+'PLN')

x=(('01','01','2018'),('01','04','2018'));
print("Data ważności "+x[0][0]+'-'+x[0][1]+'-'+x[0][2]);
print("Data ważności "+x[1][0]+'-'+x[1][1]+'-'+x[1][2]);



