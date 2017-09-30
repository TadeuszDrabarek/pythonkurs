# -*- coding: utf-8 -*-
# To jest początek programu

import os 
import fnmatch

class FO:
    def zapis(self):
        imie=input('Imię :')
        nazwisko=input('Nazwisko :')
        grupa=input('Grupa :')
        return (('%s %s %s\n') % (imie, nazwisko, grupa))
    def odczyt(self):
        f=open(self.path)
        print(f.read())
    def __init__(self,path):
        self.path=path
        while(True):
            if(os.path.exists(self.path)):
                f=open(path,'a')
                f.write(self.zapis())
                f.close()
            else:
                f=open(path,'a')
                self.zapis()
                f.write(self.zapis())
                f.close()
            q=input('Wyjście T/N:')
            if (q.upper()=='T'):
                self.odczyt()
                break

f1=FO('lista.txt')