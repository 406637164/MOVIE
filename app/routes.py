from flask import redirect, render_template,flash, url_for,request
from flask_login import login_user,login_required
from app.forms import LoginForm, RegisterForm
from app import app,bcrypt,db
from app.models import MEMBER
import cx_Oracle
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
    if user and  password:
        # login_user(user,remember=remember)
        flash("Welcome"+useremail ,category='info')
      
        return redirect(url_for('view_home'))
    flash('user not exist')

  return render_template("login.html",form=form)
def connection():
    h = '140.117.69.58' #Your host name/ip
    p = '1521' #Your port number
    sid = 'orcl' #Your sid
    u = 'GROUP11' #Your login user name
    pw = 'group11' #Your login password
    d = cx_Oracle.makedsn(h, p, sid=sid)
    conn = cx_Oracle.connect(user=u, password=pw, dsn=d)
    return conn
@app.route('/carslist',methods=["GET","POST"])
def main():
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template("carslist.html", cars = cars)

@app.route("/addcar", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblCars VALUES (:id, :name, :year, :price)", [id, name, year, price])
        conn.commit()
        conn.close()
        return  redirect(url_for("main"))

@app.route('/updatecar/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblCars WHERE id = :id", [id])
        row = cursor.fetchone()
        cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render_template("addcar.html", car = cr[0])
    if request.method == 'POST':
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        cursor.execute("UPDATE TblCars SET name = :id, year =:year, price = :price WHERE id = :id", [name, year, price, id])
        conn.commit()
        conn.close()
        return  redirect(url_for("main"))

@app.route('/deletecar/<int:id>')
def deletecar(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id = :crid", [id])
    conn.commit()
    conn.close()
    return redirect(url_for("main"))
