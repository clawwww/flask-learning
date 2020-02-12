# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 16:23
# @Author  : lt
# @Email   : 15851805363@163.com
# @File    : run3.py
# @Software: PyCharm Community Edition
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/request')
def request_views():
    #获取请求方案
    scheme = request.scheme
    method = request.method
    #获取请求方式
    args = request.args
    values = request.values
    return render_template('02-request.html',params=locals())

if __name__ == '__main__':
    app.run()