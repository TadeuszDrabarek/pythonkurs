# -*- coding: utf-8 -*-
# To jest początek programu

def silnia(n):
    wynik=1
    for i in range(2,int(n+1)):
        wynik*=i
    return wynik


def cfib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    return cfib(n-2)+cfib(n-1)

def cfib2(n):
    l=[];
    l.append(0)
    l.append(1)
    i=2;
    while(i<=n):
        l.append(l[i-2]+l[i-1])
        i+=1
    return l

def cfibsum(n):
    res=0
    for i in n:
        res+=i
    return res

print(cfib2(1118))

print(cfibsum(cfib2(1118)))


