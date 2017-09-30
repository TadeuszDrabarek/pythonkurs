# -*- coding: utf-8 -*-
# To jest początek programu

v=1;

def kolor():
    global v
    v=1-v
    return('czarny' if v else 'biały')

print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())
print(kolor())