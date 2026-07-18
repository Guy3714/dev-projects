from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Amazon Tracking Portal"

@app.route("/orders")
def orders():
    return "Echo Dot, Fire TV stick, Apple Airpods, Kindle Paperwhite"

@app.route("/order/<order_id>")
def order(order_id):
    if order_id=="Echo Dot":
        return "Name: Echo Dot, You ordered it tuesday, It is coming to you"
    elif order_id=="Fire TV stick":
        return "Name: Fire TV Stick, You ordered it wednesday, It has been delivered"
    elif order_id=="Apple Airpods":
        return "Name: Apple Airpods, You ordered it thursday, It is coming to you"
    elif order_id=="Kindle Paperwhite":
        return "Name: Kindle Paperwhite, You ordered it today, It has been delivered to you"
    



@app.route("/shipping/<ship>")
def shipping(ship):
    if ship=="California":
        return "The fee for shipping for you is $10"
    elif ship=="Texas":
        return "Your fee for shipping is $8"
    elif ship=="Flordia":
        return "Your fee for shipping is $12"
    elif ship=="New York":
        return "Your fee for shipping is $15"
    
@app.route("/delivery/<days>")
def delivery(days):
    if days==1:
        return "Same day delivery"
    elif days==2:
        return "Prime delivery"
    elif days<=5:
        return "Standerd delivery"
    elif days>5:
        return "Econmy delivery"

@app.route("/return/<order_id>/<int:days>")
def ren(order_id,days):
    if days<30:
        return f"{order_id} Return accepted!"
    else:
        return f"{order_id} Return not accepted"

if __name__=="__main__":
    app.run(debug=True) 