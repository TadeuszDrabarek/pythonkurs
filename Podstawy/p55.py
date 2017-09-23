# -*- coding: utf-8 -*-
# To jest początek programu


lista=[-1,2,3,4,5,6,7]

if (lista[0]>0 and lista[1]>0):
    print('++')
elif (lista[0]>0 and lista[1]<=0):
    print('+-')    
elif (lista[0]<=0 and lista[1]>0):
    print('-+')
elif (lista[0]>0 and lista[1]>0):
    print('++')
else:
    print('--')

