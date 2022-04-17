from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle
import os
import sys

# cx_Oracle.init_oracle_client("C:/Users/Hank Yang/AppData/Local/Programs/Python/Python39/instant_client_21_3") # init Oracle instant client 位置
# connection = cx_Oracle.connect('GROUP11', 'group11', cx_Oracle.makedsn('140.117.69.58', 1521, 'orcl')) # 連線資訊
# cursor = connection.cursor()


carsales = Flask(__name__)

def connection():
    h = '140.117.69.58' #Your host name/ip
    p = '1521' #Your port number
    sid = 'orcl' #Your sid
    u = 'GROUP11' #Your login user name
    pw = 'group11' #Your login password
    d = cx_Oracle.makedsn(h, p, sid=sid)
    conn = cx_Oracle.connect(user=u, password=pw, dsn=d)
    return conn

@carsales.route("/")
def main():
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template("carslist.html", cars = cars)
@carsales.route("/addcar", methods = ['GET','POST'])
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
        return redirect('/')
@carsales.route('/updatecar/<int:id>',methods = ['GET','POST'])
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
        return redirect('/')
@carsales.route('/deletecar/<int:id>')
def deletecar(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id = :crid", [id])
    conn.commit()
    conn.close()
    return redirect('/')


if(__name__ == "__main__"):
    carsales.run()
    carsales.debug = True
