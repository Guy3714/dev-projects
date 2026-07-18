from flask import Flask 

app=Flask(__name__)

@app.route("/")
def home():
    return "67"
    


@app.route("/check/<age>")
def STAT(age):
    age=int(age)
    if age<18:
        return "You are not old enough to vote"
    elif age>18:
        return "You are old enough to vote and drive"
if __name__=="__main__":
    app.run(debug=True)
    