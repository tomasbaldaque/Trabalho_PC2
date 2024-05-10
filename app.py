# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:29:35 2024

@author: Inês Deus
"""

from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin


app = Flask(__name__)
Userlogin.read("data/restaurante.db")
app.secret_key = 'BAD_SECRET_KEY'
import subs_login as lsub

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/login")
def login():
    return lsub.login()   

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,port=7000)
    
    