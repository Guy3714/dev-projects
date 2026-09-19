from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the movie theatere website"

@app.route("/username/int:<zone>")
def home(zone):
    return f"Hello! {zone}, the current movies we have is Avengers, intersettler, Inception, The Dark Knight"

@app.route("/<tickets>/<")