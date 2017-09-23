# -*- coding: utf-8 -*-
# To jest początek programu

a=int(input('Podaj liczbę :'))

lista=['a','b','c','d','e','f','g','h','i','j']

if (a>len(lista)-1 and (a<1)):
    print('Out of range')
else:
    print('ok, element ='+lista[a-1])

