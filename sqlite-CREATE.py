# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 11:47
# @Author  : LT
# @Email   : 15851805363@163.com
# @File    : sqlite-CREATE.py
# @Software: PyCharm Community Edition
import sqlite3
conn = sqlite3.connect("test.db")
c    = conn.cursor()
print ("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY 
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")
conn.commit()
conn.close()