# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 17:09
# @Author  : LT
# @Email   : 15851805363@163.com
# @File    : sqlite-test2.py
# @Software: PyCharm Community Edition
import sqlite3
conn = sqlite3.connect("test.db")
c    = conn.cursor()
books = [(1, 1, 'Cook Recipe', 3.12, 1),
            (2, 3, 'Python Intro', 17.5, 2),
            (3, 2, 'OS Intro', 13.6, 2),
           ]
# execute "INSERT"
c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
# using the placeholder
c.execute("INSERT INTO category VALUES (?, ?, ?)", [(2, 2, 'computer')])
# execute multiple commands
c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
conn.commit()
conn.close()
