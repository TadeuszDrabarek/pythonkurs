# -*- coding: utf-8 -*-
# To jest początek programu

sp  ={"0x01":"Myszka","0x02":"Klawiatura","0x03":"Dysk SSD","0x04":"Pendrive","0x05":"Drukarka"}
ceny={"0x01":100.50  ,"0x02":100         ,"0x03":550       ,"0x04":60        ,"0x05":222}
mag ={"0x01":15      ,"0x02":10          ,"0x03":10        ,"0x04":2000000   ,"0x05":4}
zam=[]
suma=0

while(True):
    print("Produkty:")
    for k in sp:
        print(("%6s | %-15s")%(k,sp[k]))
        
    z=input("Podaj klucz produktu, który chcesz zakupić (Q-wyjście):")
    if (z in sp.keys()):
        ilosc=int(input("Ile zamawiasz :"))
        if (ilosc>mag[z]):
            print("Niestety, nie mamy wystarczającej liczby produktów tego typu")
        else:
            zam.append(str(sp[z])+' '+str(ilosc)+' '+str(ceny[z]*ilosc))
            suma+=ceny[z]*ilosc
            mag[z]-=ilosc
    elif(z.upper()=='Q'):
        break
    else:
        print('Nie ma takiego produktu, gamoniu!')
print("Do zapłaty masz %4.2f zł" % (suma))
print(zam)