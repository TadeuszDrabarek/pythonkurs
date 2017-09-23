
zbior1=set(['k',1,False]);
zbior1.add(21)
zbior1.add('k')

print(zbior1)

print ('k' in zbior1);

print(set([1,False,'a'])<=zbior1)

A=set([1,2,3,4,5])
B=set([2,4,6,8,10])

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
