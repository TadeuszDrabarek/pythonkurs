# -*- coding: utf-8 -*-
# To jest początek programu


import pymysql
from password import password
import hashlib


class DB:
    def __init__(self):
        ok=False
        try:
            self.conn=pymysql.connect(host="localhost", user="python", passwd=password.password , db="ewidencjatest", charset='utf8') #root/root
            self.cursor=self.conn.cursor()
            ok=True
        except:
            print('Błąd połączenia z bazą danych!')
        if (ok):
            if self.login():
                while (True):
                    c=input('A-dodawanie, S-select, D-Delete, X-Zmiana hasła, Q-wyjście :').upper()
                    if (c=='A'):
                        self.ask_and_insert()
                    elif(c=='S'):
                        self.select('select * from users2')
                        print(self)
                    elif(c=='Q'):
                        print('Pa, pa ;-)')
                        break 
                    elif(c=='D'):
                        a=True
                        while(True):
                            try:
                                i=int(input('Podaj numer ID do usunięcia:'))
                                break
                            except:
                                a=False
                        if (a):
                            self.delete(i)
                        elif(c=='X'):
                            a=True
                            while(True):
                                try:
                                    i=int(input('Podaj numer ID do zmiany:'))                                                                  
                                    break
                                except:
                                    a=False
                            if (a):
                                self.select('select * from users2 where id=%i'%(i))
                                print(self)
                                im=input('Imię :')
                                na=input('Nazwisko:')
                                em=input('Email')
                                #self.update(i,im,na,em)
            else:
                print('Przekroczyłeś limit logowań!')
            self.dbclose()

    def dbclose(self):
        self.conn.close()
    def login(self):
        ile=1
        l=False
        while(True):
            user=  input('Podaj login (email) :')
            passwd=input('Podaj hasło         :')
            sql="select * from users2 where email='%s' and password='%s';"%(user,passwd)
            self.select(sql)
            if (len(self.result)>0):
                l=True
                break
            print('Błędny user lub hasło!. Masz jeszcze %i prób.'%(3-ile))
            ile+=1
            if(ile>3):
                break
        return l
    def select(self,sql):
        self.cursor.execute(sql)
        self.result=self.cursor.fetchall()

    def __str__(self):
        s='%4s|%-15s|%-20s|%-30s|%-10s\n'%('Id','Imię','Nazwisko','Email','Hasło')
        s+='-'*80+'\n'
        for row in self.result:
            s+='%4i|%-15s|%-20s|%-30s|%-10s\n'%(row[0],row[1],row[2],row[3],'*'*10)
        return s  
    def insert(self,imie,nazwisko,email,haslo):
        sql="insert into users(name,lastname,email,password) values('%s','%s','%s','%s');"%(imie,nazwisko,email,haslo)
        print(sql)
        try:
            self.cursor=self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            print('Dodano.')
        except:
            print('Błąd dodawania.')
    def ask_and_insert(self):
        imie=input('Imię :')
        nazwisko=input('Nazwisko :')
        email=input('Email :')
        haslo=input('Hasło :')
        self.insert(imie,nazwisko,email,haslo)
    def delete(self,id):
        sql="delete from users where id=%i;"%(id)
        print(sql)
        try:
            self.cursor=self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()        
            print('Usunięto.')
        except:
            print('Błąd usuwania.')

a=DB()


