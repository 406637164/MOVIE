import imp
from flask import Flask
 
from flask_sqlalchemy import SQLAlchemy
import os
import cx_Oracle
from sqlalchemy import create_engine
from app import db,login_manager
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
class TBLCARS(db.Model):
    __tablename__ = 'TBLCARS'
    ID = db.Column(db.Integer, primary_key=True)
    NAME=db.Column(db.String(100), unique=True, nullable=False)
    YEAR=db.Column(db.String(100), unique=True, nullable=False)
    PRICE=db.Column(db.Float(100), unique=True, nullable=False)
    def __init__(self,ID,NAME,YEAR,PRICE):
        self.ID = ID
        self.NAME = NAME
        self.YEAR = YEAR
        self.PRICE = PRICE
    def __repr__(self):
        return '<Member %r>' % self.NAME

@login_manager.user_loader
def load_user(user_id):
    return MEMBER.query.get(user_id)