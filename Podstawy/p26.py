
p=bool(input('Podaj p:'))
q=bool(input('Podaj q:'))

l=not(p and q)
p=(not p or not q)

print('Wynik L= ',l,'P=',l, 'L==P',l==p)

