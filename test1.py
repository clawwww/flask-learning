# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 16:13
# @Author  : LT
# @Email   : 15851805363@163.com
# @File    : test1.py
# @Software: PyCharm Community Edition

from flask import Flask

#将当前运行得到的主程序构建成Flask的应用，一边接受用户的请求（request）并给出相应（response）
app = Flask(__name__)
#路由定义
# @app.route("/")
# def hello():
#
#     return "<h1>Hello World!<h1>"

@app.route('/login')
def login():
    return "login"

#基本带参路由
@app.route('/show1/<name>')
def show1(name):
    return "%s"%name

#多参数路由
@app.route('/show2/<name>/<age>')
def show2(name,age):
    return "name:%s,age:%s"%(name,age)

#多参数路由
#类型转换器    作用
#缺省          字符串，不能有“/”
#int
#float
#path          字符串型，可以有“/”
@app.route('/show3/<name>/<int:age>')
def show3(name,age):
    return "name:%s,age:%d"%(name,age)

#多url路由匹配
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
def index(page = None):
    if page is None:
        page = 1
    return "当前页数为：%d"%page

#限定路由的请求方式
@app.route('/post',methods = ['POST','GET'])
def post():
    return "这是一个post请求"


#URL的解析
# 正向解析：升序自动解析，根据app.route()中的访问路径来匹配和处理函数
# 反向解析：通过视图处理函数的名称自动生成试图处理函数的访问路径
@app.route('/url')
def url():
    from flask import url_for
    url = url_for('show2',name = "liutian",age = "12" )
    print (url)
    resp = "<a href = '"+ url +"'>"+ url + "</a>"
    return resp


if __name__ == "__main__":
    app.run(debug=True)