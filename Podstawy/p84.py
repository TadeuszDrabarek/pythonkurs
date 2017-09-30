# -*- coding: utf-8 -*-
# To jest początek programu

import os 
import fnmatch
import datetime
import time

from time import ctime

class Dir:
    def __init__(self):
        self.L=os.listdir()
        self.cwd=os.getcwd()
        
    def najdluzszy(self):
        d=0
        f='Nie ma plików'
        for i in self.L:
            if (os.path.getsize(i))>d:
                d=os.path.getsize(i)
                q=os.path.getctime(i)
                f=i
        return ('%20s - rozmiar :%7ib - czas utworzenia :%20s')%(f,d, time.strftime('%Y/%m/%d, %H:%M:%S',time.gmtime(q)))
    
    def najstarszy(self):
        f='Nie ma plików'
        if (len(self.L)>0):
            d=time.time()
            for i in self.L:
                if (os.path.getctime(i)<d):
                    d=os.path.getctime(i)
                    q=os.path.getsize(i)
                    f=i
        return ('%20s - rozmiar :%7ib - czas utworzenia :%20s')% (f, q, time.strftime('%Y/%m/%d, %H:%M:%S',time.gmtime(d)))    

f=Dir()

print('Teraz jest :'+time.strftime('%Y/%m/%d, %H:%M:%S',time.gmtime(time.time())))
print('Najdłuższy :'+f.najdluzszy())
print('Najstarszy :'+f.najstarszy())