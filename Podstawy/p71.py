# -*- coding: utf-8 -*-
# To jest początek programu

import random

def zdanie(ile=5):
    W=['Ala','kot','ma','kota','Alę','a','ma']
    i=1
    Wy=''
    while(i<ile):
        los=random.randint(0,len(W)-1)
        if (i<ile-1):
            Wy+=W[los]+' '
        else:
            Wy+=W[los]
        i+=1
    return Wy[:1].capitalize()+Wy[1:]+'.'
    
ile=int(input('Ile wyrazów ma liczyć zdanie :'))
print(zdanie(ile))

def srednia(*arg):
    s=0
    i=0
    for n in arg:
        i+=1
        s+=n
    return s/i if (i>0) else 0

print(srednia(10,100))