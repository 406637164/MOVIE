import imp
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError 
 
# from models import MEMBER
class RegisterForm(FlaskForm):
    username =StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=8,max=20)])
    confirm = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField('Register')
    # def validate_username(self,username):
    #     member = MEMBER.query.filter_by(username=username.data).first()
    #     if member:
    #         raise ValidationError("USER NAME ALREADY TAKEN")
    # def validate_email(self,email):
    #     email = MEMBER.query.filter_by(username=email.data).first()
    #     if email:
    #         raise ValidationError("email ALREADY TAKEN")
    
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=8,max=20)])
    remember=BooleanField('Remember')
    submit = SubmitField('login')