l1=[1,3,7,15]
l2=[1,2,3,4]

s1=set()
s2=set()


for a in l1:
    s1.add(a)
    
for a in l2:
    s2.add(a)
    
s3=s1 & s2

l3=list(s3)

print (l3)