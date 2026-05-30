from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("weather.html",city="Huckleberry town",tem="78",condition="sunny",humidity="34")

if __name__=="__main__":
    app.run(debug=True)
