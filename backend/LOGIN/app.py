from flask import Flask, render_temeplate, request, redirect, url_for, session

app=Flask(__name__)

app.secret_key="my-secret-key"

@app.route("/")
def home():
    if "username" in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":

            session["username"] = username

            return redirect(url_for("home"))
        