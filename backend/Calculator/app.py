from flask import Flask

app=Flask(__name__)

#abs abosulute value

@app.route("/")
def home():
    return "67"

@app.route("/sum/<a>/<b>")
def sum(a,b):
    a=int(a)
    b=int(b)
    c=a+b
    return str(c) 

@app.route("/china/<A>/<B>")
def china(A,B):
    A=int(A)
    B=int(B)
    C=A-B
    return str(C)

@app.route("/taiwan/<Z>/<X>")
def taiwan(Z,X):
     Z=int(Z)
     X=int(X)
     W=Z*X
     return str(W)

@app.route("/India/<J>/T")
def India(J,T):
    J=int(J)
    T=int(T)
    V=T/J
    return str(V)

if __name__=="__main__":
    app.run(debug=True)