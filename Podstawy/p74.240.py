# -*- coding: utf-8 -*-
# To jest początek programu

import random

def generator(i=100):
    w=[]
    for i in range(1,i+1):
        w.append(random.randint(1,100))
    return(w)

def suma_powyzej(a,p=0):
    s=0
    j=0
    for i in a:
        if (i>p):
            s+=i
            j+=1
    return s,j

a=generator(1000)
print(suma_powyzej(a,50))