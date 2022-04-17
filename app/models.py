import imp
from flask import Flask
#  from flask.ext.sqlalchemy import SQLAlchemy<--新版取消了
from flask_sqlalchemy import SQLAlchemy
import os
import cx_Oracle
from matplotlib.pyplot import connect
from pymysql import NULL
from sqlalchemy import create_engine
from app import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 
 
#  取得目前文件資料夾路徑
# pjdir = os.path.abspath(os.path.dirname(__file__))

 

class MEMBER(db.Model):
    __tablename__ = 'MEMBER'
    MEID =db.Column(db.Integer, primary_key=True)
    MEEMAIL = db.Column(db.String(100), unique=True, nullable=False)
    MEPASSWORD=db.Column(db.String(200), unique=True, nullable=False)
    MENAME=db.Column(db.String(100), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    def __init__(self,MEEMAIL,MEPASSWORD,MENAME):
  
        self.MEEMAIL = MEEMAIL
        self.MEPASSWORD=MEPASSWORD
        self.MENAME = MENAME
    def __repr__(self):
        return '<Member %r>' % self.MENAME
    # def check_email(self, field):
    #     """檢查Email"""
    #     if MEMBER.query.filter_by(email=field.data).first():
    #         raise ValidationError('電子郵件已經被註冊過了')
class CREW(db.Model):
    __tablename__ = 'CREW'
    CID = db.Column(db.String(20), primary_key=True)
    CNAME = db.Column(db.String(20), unique=True, nullable=False)
    def __init__(self,CID,CNAME):
        self.CID = CID
        self.CNAME = CNAME
 
    def __repr__(self):
        return '<Member %r>' % self.MENAME

@login_manager.user_loader
def load_user(user_id):
    return MEMBER.query.get(user_id)