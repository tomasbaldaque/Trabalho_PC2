# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:29:35 2024

@author: Inês Deus
"""

from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin
from classes.menu import Menu
from classes.Reservas import Reserva
#fazer para todaas

app = Flask(__name__)
Userlogin.read("data/restaurante.db")
app.secret_key = 'BAD_SECRET_KEY'
import subs_login as lsub
import subs_gform as gfsub
import subs_menu as msub

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

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
     return gfsub.gform(cname)

@app.route('/about')
def about():
    return render_template('about.html', ulogin=session.get("user"))

# @app.route('/PáginaReservas')
# def PáginaReservas():
#     return render_template('PáginaReservas.html', ulogin=session.get("user"))

@app.route('/menu')
def menu():
    return msub.chkmenu()

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,port=7000)
    

    
    
    
    
    
