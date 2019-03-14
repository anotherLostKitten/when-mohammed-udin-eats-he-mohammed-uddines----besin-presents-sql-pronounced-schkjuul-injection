#"When Mohammed Uddin eats he Mohammed Uddines"-- Besin presents: Sql (pronounced schkjuul) injection's only comment in all of their python file, feast your eyes while it lasts.
from urllib import request, parse
import json
import sqlite3
from string import ascii_letters,digits
from os import urandom,remove
from random import randint
from flask import Flask,render_template,request,flash,redirect,url_for,make_response,Request,session
app=Flask(__name__)
app.secret_key=urandom(32)
@app.route("/")
def home():
    if "user"in session:
        return redirect("/schkjuul")
    return render_template("home.html")
@app.route("/schkjuul",methods=["GET","POST"])
def login():
    db=sqlite3.connect("/var/www/sqlinject/sqlinject/util/users.db")
    squul=db.cursor()
    if not"user"in session:
        if request.method=="GET"or"user"not in request.form or"pass"not in request.form:
            return redirect("/")
        if not logcheck(request.form["user"],request.form["pass"],squul):
            flash("User or pass is the not good.")
            return redirect("/")
        session["user"]=request.form["user"]
    tmp=userinf(session["user"],squul)
    db.close()
    u = session["user"]
    if "sql_user" in request.form:
        nudeb=sqlite3.connect("/var/www/sqlinject/sqlinject/util/"+u+".db")
        nusquul=nudeb.cursor()
        user = request.form["sql_user"]
        pwd = request.form["sql_pass"]
        try:
            try:
                ulog = nusquul.execute('SELECT user FROM users WHERE user = "' + user + '" AND pass = "' + pwd + '";').fetchone()
                if ulog!=None:
                    flash("Logged in as "+ulog[0]+"!")
                else:
                    flash("Bad username or password")
            except sqlite3.Warning:
                flash("Sql operations did not return a value")
                nusquul.executescript('SELECT user FROM users WHERE user = "' + user + '" AND pass = "' + pwd + '";')
        except sqlite3.OperationalError:
            flash("Sql operational error")
        nudeb.commit()
        nudeb.close()
    return render_template("sql.html",sqltable=usersql(session["user"]),userinf=tmp)
@app.route("/resetudb")
def rdbuthingbazinga():
    if "user" in session:
        usersqlify(session["user"])
        flash("Database reset")
    return redirect("/schkjuul")
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect("/")
@app.route("/registerr",methods=["GET","POST"])
def registerr():
    print(request.form)
    if "user"not in request.form or"pass"not in request.form:
        return redirect("/")
    print(request.form)
    if "users"==request.form["user"]or not all(i in(ascii_letters+digits)for i in request.form["user"]):
        flash("User must be strictly alphanumeric.")
        return redirect("/")
    db=sqlite3.connect("/var/www/sqlinject/sqlinject/util/users.db")
    squul=db.cursor()
    if userinf(request.form["user"],squul)!=None:
        flash("User already exists.")
        db.close()
        return redirect("/")
    squul.execute("INSERT INTO users VALUES(?, ?, ?);",(squul.execute("SELECT COUNT(*) FROM users;").fetchone()[0],request.form["user"],request.form["pass"]))
    db.commit()
    db.close()
    usersqlify(request.form["user"])
    session["user"]=request.form["user"]
    return redirect("/schkjuul")
def logcheck(u,p,squul):
    try:
        return p==squul.execute("SELECT pass FROM users WHERE user = ?;",(u,)).fetchone()[0]
    except TypeError:
        return False
def userinf(u,squul):
    return squul.execute("SELECT * FROM users WHERE user = ?;",(u,)).fetchone()
def usersql(u):
    nudeb=sqlite3.connect("/var/www/sqlinject/sqlinject/util/"+u+".db")
    nusquul=nudeb.cursor()
    try:
        b=nusquul.execute("SELECT * FROM users;").fetchall()
    except sqlite3.OperationalError:
        b=None
    nudeb.close()
    return b
def usersqlify(u):
    try:
        remove("/var/www/sqlinject/sqlinject/util/"+u+".db")
    except FileNotFoundError:
        pass
    nudeb=sqlite3.connect("/var/www/sqlinject/sqlinject/util/"+u+".db")
    nusquul=nudeb.cursor()
    nusquul.execute("CREATE TABLE users (userid INTEGER PRIMARY KEY, user TEXT, pass TEXT);")
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(0,"Mohammed Uddin","Zbunzzrq Hqqva"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(1,"AzureLobster","NmherYbofgre"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(2,"BidOOF","OvqBBS"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(3,"Discord Admin","Qvfpbeq Nqzva"))
    nudeb.commit()
    nudeb.close()
def reset():
    db=sqlite3.connect("/var/www/sqlinject/sqlinject/util/users.db")
    squul=db.cursor()
    try:
        for i in squul.execute("SELECT user FROM users;").fetchall():
            try:
                remove("/var/www/sqlinject/sqlinject/util/"+i[0]+".db")
            except FileNotFoundError:
                pass
    except sqlite3.OperationalError:
        pass
    squul.execute("DROP TABLE IF EXISTS users;")
    squul.execute("CREATE TABLE users (userid INTEGER, user TEXT, pass TEXT);")
    db.commit()
    db.close()
if __name__=="__main__":
    reset()
    app.debug=True
    app.run()
reset()
