from flask import flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to skyline airlines"

@app.route("/flights")
def skyline():
    return "Aviable flights: New york, Los Angeles, Chicago, Miami"

@app.route("/flights/<destination>")
def airport(destination):
    if destination=="New York":
        return "Destination: New York, Departure time: 3:00 AM, Gate number: 31"
    elif destination=="Los Angeles":
        return "Destination: Los Angeles, Departure time: 3:00 PM, Gate number: 27"
    elif destination=="Chicago":
        return "Destination: Chicago, Departure time: 7:00 PM, Gate number: 43"
    elif destination=="Miami":
        return "Destination: Miami, Departure time: 5:00 AM, Gate number: 56"
    else:
        return "Unvalid location"
    
@app.route("/checkin/<passenger>")
def sixseven(passenger):
    return f"{passenger}, your check in was succesful, board in generating"

@app.route("/baggage/<int:weight>")
def sevensix(weight):
    if weight<20:
        return "No extra fee"
    elif weight>20:
        return "$50 fee"
    elif weight>31:
        return "$100 fee"
    else:
        return "Non valid entry"
    
@app.route("/seat/<type>")
def five(type):
    if type=="economy":
        return "$0"
    elif type=="prenium economy":
        return "$40"
    elif type=="Business":
        return "$150"
    elif type=="First class":
        return "$300"
    else:
        "Not valid seat type"

@app.route("/boarding/<int:minutes>")
def four(minutes):
    if minutes>30:
        return "Boarding not started"
    elif minutes<30:
        return "Boarding started"
    elif mintutes<11:
        return "Final call"
    else:
        "Not valid entry"

@app.route("/summary/<passenger>/<destination>")
def SWEET(passenger, destination):
    return f"Passenger's name is {passenger}, their destination is {destination}"

if __name__=="__main__":
    app.run(debug=True) 