# -*- coding: utf-8 -*-
# To jest początek programu

for x in range(5,100,10):
    print("%4i=%6i=%8i" % (x,x**2,x**3))
    
for v in range(-10,20,1):
    print('Temperatura: %0+4i, temp*0.33: %5.2f ' % (v,v*0.33))
    
for i in (range(0,100,1)):
    if (i%3!=0):
        continue
    print(i)
    
for i in (range(0,100,1)):
    if (i==13):
        break                   # break = wyjście z pętli
    if (i%3!=0):
        continue                # continue = przerwanie tej iteracji i kontynuacja pętli z kolejną wartością
    print(i)