# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:29:35 2024

@author: Inês Deus
"""

from flask import Flask, render_template, request, session


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,port=7000)