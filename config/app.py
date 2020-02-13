# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 17:51
# @Author  : lt
# @Email   : 15851805363@163.com
# @File    : app.py
# @Software: PyCharm Community Edition
from flask import Flask
from config.settings  import config,get_app_config

def create_app(config_name=None):
    # 不指定config_name，默认取配置文件FLASK_CONFIG的值
    # 指定config_name，则以指定的环境为主
    if config_name is None:
        config_name=get_app_config('FLASK_CONFIG')
    app = Flask(__name__)
    cfobj=config[config_name]
    app.config.from_object(cfobj)

    return app

#测试不指定config_name
app = create_app()
print(app.config['FLASK_ENV'])
print(app.config['AAA'])
print('*'*50)
#测试指定config_name
app = create_app('development')
print(app.config['FLASK_ENV'])
print(app.config['AAA'])