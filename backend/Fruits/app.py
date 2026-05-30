from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    fruit_list = ["Apple", "Mango", "Banana", "Orange"]

    return render_template("index.html", fruits=fruit_list)

app.run(debug=True)