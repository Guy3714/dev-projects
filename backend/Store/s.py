from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
        return render_template(home)

@app.route("/product")
def product():
    return render_template(product)

@app.route("/contact")
def contact():
      return render_template(contact)