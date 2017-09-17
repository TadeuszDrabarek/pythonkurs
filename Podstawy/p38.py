# -*- coding: utf-8 -*-

spk = float(input('Podaj SPK :'));
r = float(input('Podaj stopę procentową :'));
n = float(input('Podaj liczbę lat :'));
i = float(input('Podaj inflację :'));
rp=(r-i)/(1+i)

wynik=spk*((1+rp)**n)


print(round(wynik,2))





