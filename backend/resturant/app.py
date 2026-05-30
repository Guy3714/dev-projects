from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",name="back air")

@app.route("/menu")
def scribe():
    return render_template("menu.html")

@app.route("/about")
def bcribe():
    return render_template("about.html")

@app.route("/contact")
def Wcribe():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)