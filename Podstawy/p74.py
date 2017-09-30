# -*- coding: utf-8 -*-
# To jest początek programu


def srednia(*arg):
    s=0
    for n in arg:
        s+=n
    return s/len(arg) if (len(arg)>0) else 0.0

print(srednia(10,100))
print(srednia(1))
print(srednia())
