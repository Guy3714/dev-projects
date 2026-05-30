from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("movies.html",name="movie1",name2="movie2",name3="movie3",number="5",number2="6",number3="7")

if __name__=="__main__":
    app.run(debug=True) 