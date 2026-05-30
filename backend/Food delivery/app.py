from flask import Flask

qpp=flask(__name__)

@app.route("/")
def home():
    return "welcome to foodpress"

@app.route("/menu/<item>")
def Imenu(item):
    item=int(item)
    return f"You ordered {item}"

@app.route("/delivery/<int:distance>")
def Deli():
    distance=int(distance)
    if distance<5:
        return "Order will come in 10 minutes"
    elif distance>5:
        return "Order will come in 30 mintues"
    elif distance>15:
        return "Order will come in 60 minutes"

@app.route("/bill/<int:amount")
def Emount(amount):
    amount=int(amount)
    if amount>1000:
        return f"discount applied {amount-200}"
    elif amount>500:
        return f"discount applied {amount-200}"
    else:
        return f"No discount {amount}"

@app.route("/status/<status")
def Satus(status):
    status=int(status)
    if status=preparing:
        return "Your food is being prepared"
    elif status=out:
        return "Out for delivery"
    else:
        return "UHHH 67 HAHAHAHAHA"