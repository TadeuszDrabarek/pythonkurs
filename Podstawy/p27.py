# -*- coding: utf-8 -*-

a=False
b=False
c=True

g1=not a and not b and not c
g2=not a and not b and c
g3=not a and b and not c
g4=a and not b and not c

w=g1 or g2 or g3 or g4

print(w)

print(ord('ą'))

print(chr(261))