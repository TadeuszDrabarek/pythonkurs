# -*- coding: utf-8 -*-
# To jest początek programu
import random

wylosowane=set()  
# tworzymy pusty zbiór

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

liczba=random.randint(1,49)
wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
print(wylosowane)

if len(wylosowane)==6:
    print("Zbiór jest wypełniony")
elif len(wylosowane)==5: 
    print("Dobieram jeden element")
    liczba=random.randint(1,49)
    wylosowane.add(liczba)          # dodajemy wylosowaną liczbę do zbioru
    print(wylosowane)
else:
    print('Mniej niż 5')