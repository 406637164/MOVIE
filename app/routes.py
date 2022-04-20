from flask import redirect, render_template,flash, url_for,request
from flask_login import login_user,login_required
from app.forms import LoginForm, RegisterForm
from app import app,db
from app.models import MEMBER
from app.models import TBLCARS
from sqlalchemy import create_engine
# import cx_Oracle
@app.route("/")

def view_home():
  return render_template("index.html" )

@app.route('/register',methods=["GET","POST"])  
def register():  
  form=RegisterForm()
  if form.validate_on_submit():
      # pass
      username=form.username.data
      email = form.email.data
      password =form.username.data
      members=MEMBER(MENAME=username,MEEMAIL=email,MEPASSWORD=password)
      db.session.add(members)
      
      db.session.commit()
      flash('歡迎'+username, category='success')
      # print(username,email,password)
      return redirect(url_for("view_home"))
  return render_template('register.html',form=form)  

@app.route('/login',methods=["GET","POST"])
 
def login():
  form = LoginForm()
  if form.validate_on_submit():
    useremail=form.email.data
    password =form.password.data 
    remember = form.remember.data
    user=MEMBER.query.filter_by(MEEMAIL=useremail).first()
    passds=MEMBER.query.filter_by(MEPASSWORD=password).first()
    if useremail=="root@gmail.com" and  password=="12345678":   
        return redirect(url_for('main'))
    if user and  password:
        # login_user(user,remember=remember)
        flash("登入成功",category='info')
      
        return redirect(url_for('view_home'))
    # flash('user not exist')

  return render_template("login.html",form=form)

# def connection():
   
#     host="140.117.69.58"
#     port=1521
#     sid='orcl'
#     user='Group11'
#     password='group11'
#     sid = cx_Oracle.makedsn(host, port, sid=sid)
#     cstr = 'oracle://{user}:{password}@{sid}'.format(
#         user=user,
#         password=password,
#         sid=sid
#     )
    
#     conn =  create_engine(
#         cstr,
#         convert_unicode=False,
#         pool_recycle=10,
#         pool_size=50,
#         echo=True
#     )
#     # cx_Oracle.init_oracle_client("C:\flasks\app\instantclient_21_3", config_dir=r"C:\flasks\app")
#     return conn

@app.route('/carslist',methods=["GET","POST"])
def main():
    cars = []
    # conn = connection()
    # con = conn.connect()
    # cursor = conn.cursor()
    car=TBLCARS.query.all()
    for row in car:
        cars.append({"id": row.ID, "name": row.NAME, "year": row.YEAR, "price": row.PRICE})
        print(cars)
    # output=con.execute("SELECT * FROM TblCars")
    # for row in output.fetchall():
    #     cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    # con.close()
    return render_template("carslist.html", cars = cars)

@app.route("/addcar", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
     
        ids = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        car=TBLCARS(ID=ids,NAME=name,YEAR=year,PRICE=price)
        db.session.add(car)
        db.session.commit()
        db.session.close()
        # conn = connection()
        # cursor = conn.cursor()
        # con1 = conn.connect()
        # con1.execute("INSERT INTO TblCars VALUES (:id, :name, :year, :price)", [id, name, year, price])
        
        # con1.commit()
        # conn.close()
        return  redirect(url_for("main"))

@app.route('/updatecar/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    cr = []
 
    if request.method == 'GET':
     
        car=TBLCARS.query.filter_by(ID=id).first()
       
        cr.append({"id": car.ID, "name": car.NAME, "year": car.YEAR, "price":car.PRICE})
    
        return render_template("addcar.html", car = cr[0])
    if request.method == 'POST':
        ids= int(request.form["id"])
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        car=TBLCARS.query.filter_by(ID=id).update({'ID':  ids,"NAME": name, "YEAR": year,"PRICE":price})
      
        db.session.commit()
        db.session.close()
       
        return  redirect(url_for("main"))

@app.route('/deletecar/<int:id>')
def deletecar(id):
    todo=TBLCARS.query.filter_by(ID=id).first()
    db.session.delete(todo)
    db.session.commit()
 
    return redirect(url_for("main"))
