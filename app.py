#"When Mohammed Uddin eats he Mohammed Uddines"-- Besin presents: Sql (pronounced schkjuul) injection's only comment in all of their python file, feast your eyes while it lasts.
from urllib import request, parse
import json
import sqlite3
from string import ascii_letters,digits
from os import urandom,remove
from random import randint
from flask import Flask,render_template,request,flash,redirect,url_for,make_response,Request
app=Flask(__name__)
app.secret_key=urandom(32)
DB_FILE=url_for("util",filename="users.db")
db=sqlite3.connect(DB_FILE)
squul=db.cursor()
@app.route("/")
def home():
    if "user"in session:
        return redirect("/schkjuul")
    return render_template("home.html")
@app.route("/schkjuul",methods=["GET","POST"])
def login():
    if not"user"in session:
        if request.method=="GET"or"username"not in request.form:
            return redirect("/")
        if not logcheck(request.form["username"],request.form["password"]):
            flash("Username or password is the not good.")
            return redirect("/")
        session["user"]=request.form["username"]
    return render_template("sql.html",sqltable=usersql("username"),userinf=userinf(session["user"])))
@app.route("/registerr",methods=["GET","POST"])
def registerr():
    if request.method=="GET"or"username"not in request.form or"password"not in request.form:
        return redirect("/")
    if"users"==request.form["username"]or not all(i in(ascii_letters+digits)for i in request.form["username"]):
        flash("Username must be strictly alphanumeric.")
        return redirect("/")
    squul.execute("INSERT INTO users VALUES(?, ?, ?);",(squul.execute("SELECT COUNT(*) FROM users;").fetchone[0],request.form["username"],request.form["password"]))
    squul.commit()
    usersqlify(request.form["username"])
    return redirect("/schkjuul")
def logcheck(u,p):
    return p==squul.execute("SELECT password FROM users WHERE username = ?;",(u,)).fetchone()[0]
def userinf(u):
    return squul.execute("SELECT * FROM users WHERE username = ?;",(u,)).fetchone()
def usersql(u):
    nudeb=sqlite3.connect(url_for("util/",filename=u+".db"))
    nusquul=nudeb.cursor()
    b=nusquul.execute("SELECT * FROM sql;").fetchall()
    nudeb.close()
    return b
def usersqlify(u):
    remove(url_for("util",filename=u+".db"))
    nudeb=sqlite3.connect(url_for("util/",filename=u+".db"))
    nusquul=nudeb.cursor()
    nusquul.execute("CREATE TABLE users (userid INTEGER PRIMARY KEY, username TEXT, password TEXT);")
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(0,"Mohammed Uddin","Zbunzzrq Hqqva"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(1,"AzureLobster","NmherYbofgre"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(2,"BidOOF","OvqBBS"))
    nusquul.execute("INSERT INTO users VALUES(?, ?, ?);",(3,"Discord Admin","Qvfpbeq Nqzva"))
    nusquul.commit()
    nudeb.close()
def reset():
    squul.execute("DROP TABLE IF EXISTS users;")
    squul.execute("CREATE TABLE users (userid INTEGER PRIMARY KEY, username TEXT, password TEXT);")
    squul.commit()
if __name__=="__main__":
    app.debug=True
    app.run()
