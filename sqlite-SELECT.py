# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 11:50
# @Author  : LT
# @Email   : 15851805363@163.com
# @File    : sqlite-SELECT.py
# @Software: PyCharm Community Edition
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("Opened database successfully")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()