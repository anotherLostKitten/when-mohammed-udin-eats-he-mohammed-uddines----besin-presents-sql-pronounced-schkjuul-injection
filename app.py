from urllib import request, parse
import json
import sqlite3
from string import ascii_letters,digits
from os import urandom
from random import randint

from flask import Flask, render_template, request, flash, redirect, url_for, make_response, Request

app = Flask(__name__)

app.secret_key = urandom(32)

DB_FILE = "users.db"
db = sqlite3.connect(DB_FILE)
squul = db.cursor()

@app.route("/")
def home():
    if "user" in session:
        return redirect("/schkjuul")
    return render_template("home.html")

@app.route("/schkjuul",methods=["POST"])
def login():
    if not "user" in session:
        if"username"not in request.form:
            return redirect("/")
        if not logcheck(request.form["username"],request.form["password"]):
            flash("Username or password is the not good.")
            return redirect("/")
        session["user"]=request.form["username"]
    try:
        sl=int(request.form["slide_location"])
    except TypeError:
        sl=0
    return render_template("sql.html", sqltable=usersql("username"), userinf=userinf(session["user"]),slide_location=sl)
@app.route("/registerr",methods=["GET","POST"])
def registerr():
    if request.method=="GET" or "username" not in request.form:
        return redirect("/")
    if"users"==request.form["username"]or not all(i in(ascii_letters+digits)for i in request.form["username"]):
        flash("Username must be strictly alphanumeric.")
        return redirect("/")
    #things things things TODO
    return redirect("/schkjuul")

def logcheck(u,p):
    return p==squul.execute("SELECT password FROM users WHERE username = ?;", (u,)).fetchone()[0]
def userinf(u):
    return squul.execute("SELECT * FROM users WHERE username = ?;", (u,)).fetchone()
def usersql(u):
    nudeb=sqlite3.connect("udb/"+u+".db")
    nusquul=nudeb.cursor()
    b=nusquul.execute("SELECT * FROM sql;").fetchall()
    nudeb.close()
    return b
def reset():
    squul.execute("DROP TABLE IF EXISTS users;")
    squul.execute("CREATE TABLE users (userid INTEGER PRIMARY KEY, username TEXT, password TEXT);")

if __name__ == "__main__":
    app.debug = True
    app.run()
