
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def hello_world():
    score = 20
    return render_template("index.html"),score



if __name__ == '__main__':
   app.run(debug = True)
