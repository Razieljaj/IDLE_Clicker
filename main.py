
from flask import Flask, render_template, request, redirect, url_for
from bdd import *

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        donnees = request.form
        pseudo = donnees.get('pseudo')
        password = donnees.get("password")
        if create_account(pseudo, password) == True:
            return redirect(url_for('home'))
        else:
            error_message = "Pseudo already taken, please choose another one."
            return render_template("connect.html", error_message = error_message, pseudo = pseudo)
    return render_template("connect.html")

@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        donnees = request.form
        pseudo = donnees.get('pseudo')
        password = donnees.get("password")
        if login_account(pseudo, password) == True:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template("login.html")

score = 0

@app.route("/home",methods=['GET', 'POST'])
def home():
    global score
    if request.method == "POST":
        score = score + 1
        return redirect(url_for("home"))
    return render_template("index.html",score = score)



if __name__ == '__main__':
    app.run(debug = True)