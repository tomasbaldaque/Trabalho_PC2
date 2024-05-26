from flask import Flask, render_template, request, session
from classes.menu import Menu

def chkmenu():
    ulogin=session.get("user")
    if (ulogin != None):
        print(request.args)
        if 'nome' in request.args.keys():
            nome = request.args.get("nome")
            obj = Menu.find(nome)
            return render_template("menu.html", ulogin=session.get("user"), obj = obj)
        else:
            return render_template("menu.html", ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
    
