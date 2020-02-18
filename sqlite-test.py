# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 10:05
# @Author  : LT
# @Email   : 15851805363@163.com
# @File    : sqlite-test.py
# @Software: PyCharm Community Edition
# 创建一个访问数据库test.db的连接
import sqlite3

if __name__ == "__main__":
    # SQLiteCase01.db is a file in the working directory.
    conn = sqlite3.connect("SQLiteCase01.db")  # 在此文件所在的文件夹打开或创建数据库文件
    c = conn.cursor()  # 设置游标
    # create tables 创建一个含有id，name，password字段的表category和book
    c.execute('''CREATE TABLE category
          (id int primary key, 
          sort int, 
          name text)''')
    c.execute('''CREATE TABLE book
          (id int primary key, 
           sort int, 
           name text, 
           price real, 
           category int,
           FOREIGN KEY (category) REFERENCES category(id))''')
    # save the changes
    conn.commit()  # python连接数据库默认开启事务，所以需先提交
    # close the connection with the database
    conn.close()  # 关闭连接
