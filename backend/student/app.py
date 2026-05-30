from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("movies.html",name="movie1",,number2="6",)

if __name__=="__main__":
    app.run(debug=True) 