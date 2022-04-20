import email
import imp
from multiprocessing import connection
from os import stat
import re
from ssl import MemoryBIO
from unicodedata import name
from unittest import result
from flask import Flask,redirect,flash
from flask import request
import json

from flask import render_template
from flask import session
import flask
from flask_bootstrap import Bootstrap
from datetime import datetime, date
import cx_Oracle
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask_login import LoginManager
 
import os
# from app.forms import RegisterForm
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt
# from models import MEMBER
app = Flask(__name__)
host="140.117.69.58"
port=1521
sid='orcl'
user='Group11'
password='group11'
sid = cx_Oracle.makedsn(host, port, sid=sid)
cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)
engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)
# result=engine.execute('select * from MOVIELIST')
# for row in result:
#     print(row) 
 
# engine.execute('INSERT INTO MEMBER (MEID, MEEMAIL,MEPASSWORD,MENAME) VALUES (:MEID, :MEEMAIL,:MEPASSWORD,:MENAME)', MEID = 1, MEEMAIL = "PETER100@gmail.com",MEPASSWORD="lpasdpls123456",MENAME="ppepe123")
 
  #建立application
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://Group11:1521/orcl'
# db.init_app(app)
# app =Flask(__name__
#             ,static_folder="static", #靜態檔案的資料夾名稱
#             static_url_path="/",template_folder="templates") #靜態檔案對應的網址路徑
# app=flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
# app.config.from_object(Config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = cstr
app.config['SECRET_KEY'] = 'the random string' 
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message='yot must log in'
login_manager.login_message_category='info'
bcrypt = Bcrypt(app)
# app.config.from_object(Config)
print("secced")
from app.routes import *


