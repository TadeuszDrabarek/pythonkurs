# -*- coding: utf-8 -*-
# To jest początek programu

import pymysql

def lustrzana(a):
    s=str(a)
    i=len(s)
    j=(i//2 if (i%2==0) else i//2-1)
    w=True
    k=0
    #print('s,i,j,k',s,i,j,k)
    while(k<j):
        if (s[k]!=s[i-1-k]):
            #print(k,s[k],i-1-k,s[i-1-k])
            w=False
            break
        k+=1
    return w
        
liczba=input('Podaj liczbe :')
print(liczba[::-1])   # tak też można odwrócić

print(lustrzana(liczba))