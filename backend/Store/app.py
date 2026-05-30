from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to freshmart grocceray store"

@app.route("/product/<item>")
def ITEMS(item):
    if item=="apple":
        return "This item is $1.20"
    elif item=="milk":
        return "This item is $0.60"
    elif item=="bread":
        return "This item is $0.40"
    else:
        return "We don't have this item"

@app.route("/discounts/<int:amount>")
def AMOUNT(amount):
    amount=int(amount)
    if amount>500:
        return 'You get a 20 percent discount'
    elif amount<200:
        return "No discount for you"
    else:
        return "10 percent discount"


@app.route("/bill/<item>/<int:qty>")
def QTY(item,qty):
    qty=int(qty)
    if item=="apple":
        return "Your bill is $1.20"
    elif item=="milk":
        return "Your bill is $0.60"
    elif item=="bread":
        return "Your bill is $0.40"

if __name__=="__main__":
    app.run(debug=True)