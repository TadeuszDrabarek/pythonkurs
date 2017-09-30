# -*- coding: utf-8 -*-
# To jest początek programu
import random

def wykres(znak='*',ile=10,szerokosc=10):
    for i in range(0,ile):
        x=random.randint(1,szerokosc)
        print('%20s|%-20s' % (znak*x,znak*x))

def html(napis,color='',font_size='',font_weight=''):
    print('<span style="color=%s; font-size=%s; font-weight=%s">%s</span>'%(color,font_size,font_weight,napis))

wykres('=',szerokosc=20,ile=15);

html("To jest napis",color='red',font_size='8px',font_weight='dupa')