
from flask import Flask, render_template, request, redirect, url_for, session
from bdd import *

app = Flask(__name__)
app.secret_key = "super_secret_key(&è'çè)"

@app.route("/",methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        donnees = request.form
        pseudo = donnees.get('pseudo')
        password = donnees.get("password")
        if create_account(pseudo, password) == True:
            session["pseudo"] = pseudo
            return redirect(url_for('home'))
        else:
            error_message = "Pseudo already taken, please choose another one."
            return render_template("connect.html", error_message = error_message, pseudo = pseudo)
    return render_template("connect.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        donnees = request.form
        pseudo = donnees.get('pseudo')
        password = donnees.get("password")
        user = login_account(pseudo, password)

        if user:
            session["pseudo"] = pseudo
            return redirect(url_for('home'))
        else:
            error_message = "This account does not exist, correct your mistake or create a new one."
            return render_template("login.html", error_message=error_message, pseudo=pseudo)

    return render_template("login.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    if "pseudo" in session:
        pseudo = session["pseudo"]
        user_id = get_user_id(pseudo)
        data_user = get_user_data(user_id[0][0])
        if request.method == "POST":
            score_rise(user_id[0][0])
            return render_template("index.html", data_user = data_user)
        
        return render_template("index.html", data_user = data_user)
    else:
        return redirect(url_for("login"))




if __name__ == '__main__':
    app.run(debug = True)