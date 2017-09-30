# -*- coding: utf-8 -*-
# To jest początek programu
import random

def wykres(znak='*',ile=10,szerokosc=10):
    for i in range(0,ile):
        x=random.randint(1,szerokosc)
        print('%20s|%-20s' % (znak*x,znak*x))


wykres('=',szerokosc=20,ile=15);