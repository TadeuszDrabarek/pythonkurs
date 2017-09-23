# -*- coding: utf-8 -*-
# To jest początek programu


i1 = input('Podaj imię 1 :');
i2 = input('Podaj imię 2 :');

if (i1.isdigit()):
    print("Imie 1 składa się z samych cyfr")
elif (i2.isdigit()):
    print("Imie 2 składa się z samych cyfr")
else:
    if (i1.upper()==i2.upper()):
        print("Identycznie")
    elif (i1.upper()<i2.upper()):
        print("I1<I2")
    elif (i1.upper()>i2.upper()):
        print("I1>I2")

print(i1,i2)



