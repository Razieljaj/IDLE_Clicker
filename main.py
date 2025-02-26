
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/home",methods=['GET', 'POST'])
def home():
    score = 0
    if request.method == "POST":
        if request.form['click'] == 3:
	        score = score + 1
    return render_template("index.html",score = score)



if __name__ == '__main__':
    app.run(debug = True)
