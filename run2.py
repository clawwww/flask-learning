# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 11:08
# @Author  : lt
# @Email   : 15851805363@163.com
# @File    : run2.py
# @Software: PyCharm Community Edition

from flask import Flask, render_template

app = Flask(__name__)
# 什么是模板
# 模板是一个包含响应文本的文件（通常是html）该文件中允许包含“占位变量”来表示动态的内容，其具体值在请求中才能知道。“占位变量”最终会被真是的值所替换。
# 模板最终也会被解析成相应的字符串，称为“渲染”。
# flask实际上是用jinja2强大的模板引擎
# 模板的设置
# 默认情况下Flask会在程序文件夹中的templates子文件夹中寻找模板
# 渲染模板
# 在视图函数中，通过
# return render_template()将模板渲染成字符串再响应给客户端
# rander_tmplate()语法：
# Rander_template('XXX.html',arg1 = value1,arg2 = value2)
# 参数2可以省略
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()