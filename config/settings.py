# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 17:50
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : settings.py
# @Software: PyCharm Community Edition
import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))
cfgpath = os.path.join(basedir, 'config.ini')
cf = ConfigParser()
cf.read(cfgpath)

# 获取邮件配置
def get_email_config(option):
    return cf.get('email', option)

# 获取邮件配置
def get_app_config(option):
    return cf.get('app', option)

# 获取数据库配置
def get_sqlalchemy_config(option):
    return cf.get('sqlalchemy', option)

# 获取生产环境配置
def get_production_config(option):
    return cf.get('production', option)

# 获取开发环境配置
def get_development_config(option):
    return cf.get('development', option)

class BaseConfig(object):
    SECRET_KEY = get_app_config('SECRET_KEY')

    SQLALCHMEY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = get_email_config('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = get_email_config('MAIL_USERNAME')
    MAIL_PASSWORD = get_email_config('MAIL_USERNAME')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    AAA = 'in DevelopmentConfig'
    SQLALCHEMY_DATABASE_URI = get_development_config('DATABASE_URL')


class ProductingConfig(BaseConfig):
    FLASK_ENV = 'production'
    AAA='in ProductingConfig'
    SQLALCHEMY_DATABASE_URI = get_production_config('DATABASE_URL')

config = {
    'production': ProductingConfig,
    'development': DevelopmentConfig
}