from flask import Flask

app=flask(__name__)

@app.route("/")
def home():
    return "THATS A DEAL"

@app.route("discount/<cost>")
def STAT(cost):
    cost=int(cost)
    if cost<1000:
        return "No discount"
    elif cost>1000:
        return "1/10 discount"
    elif cost>4999:
        return "2/10 discount"
    
if __name__=="__main__":
    app.run(debug=True)