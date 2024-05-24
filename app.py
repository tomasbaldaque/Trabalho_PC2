# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:29:35 2024

@author: Inês Deus
"""

from flask import Flask, render_template, request, session
from classes.userlogin import Userlogin
from classes.menu import Menu
from classes.Reservas import Reserva
from classes.pedidos import Pedido 

app = Flask(__name__)
Userlogin.read("data/restaurante.db")   # Lê os dados de login de usuário de um banco de dados
app.secret_key = 'BAD_SECRET_KEY'   # Chave secreta usada para sessões (deve ser uma chave forte em produção)
import subs_login as lsub      # Importa o módulo de login
import subs_gform as gfsub     # Importa o módulo de formulários gerais
import subs_menu as msub       # Importa o módulo de menu

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))    # Renderiza a página inicial e passa a informação de login de usuário (se houver)

@app.route("/login")
def login():
    return lsub.login()   # Chama a função de login do módulo de login

@app.route("/logoff")
def logoff():
    return lsub.logoff()    # Chama a função de logoff do módulo de login

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()     # Verifica as credenciais de login usando o módulo de login

@app.route("/gform/<cname>", methods=["post","get"])  
def gform(cname=''):
     return gfsub.gform(cname)  # Renderiza um formulário baseado no nome passado como parâmetro


@app.route('/about')
def about():
    return render_template('about.html', ulogin=session.get("user"))  # Renderiza a página "About" e passa a informação de login de usuário (se houver)


@app.route('/PáginaReservas')
def PáginaReservas():
   return render_template('PáginaReservas.html', ulogin=session.get("user"))

@app.route('/menu')
def menu():
    return msub.chkmenu()     # Chama a função de menu do módulo de menu

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=False,port=7000)     # Executa o aplicativo no modo de produção (debug desativado) na porta 7000
    

    
    
    
    
    
