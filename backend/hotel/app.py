from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to hotelly hotel"

@app.route("/rooms")
def Krit():
    return "Business:$75, Business+:$125, Peak cinema(or PC for short):$175   The fee's are daily"

@app.route("/room/<room_type>")
def crit(room_type):
    if room_type=="Business":
        return "Room type:Business, Price per night:$75, Maximum occupacy:5 people, Avabillity: 4 rooms avabilbe"
    elif room_type=="Business+":
        return "Room type:Business+, Price per night:$125, Maximum occupacy:5 people, Avabillity 9 rooms avabilbe"
    elif room_type=="Peak cinema":
        return "Room type:Peak cinema(PC for short), Price per night:$175, Maximum occupacy: 4 people, Avabillity 2 rooms avabilbe"
    elif room_type=="PC":
        return "Room type:Peak cinema(PC for short), Price per night:$175, Maximum occupacy: 4 people, Avabillity 2 rooms avabilbe"
    else:
        return "Not valid room type"

@app.route("/book/<room_typ1e>/<int:nights>")
def booker(room_typ1e, nights):
    B=nights*75
    C=nights*125
    D=nights*175
    if room_typ1e=="Business":
        return f"Room type:Business, Nights:{nights}, Total cost:${B}"
    elif room_typ1e=="Business+":
        return f"Room type:Business+, Nights:{nights}, Total cost:${C}"
    elif room_typ1e=="Peak cinema":
        return f"Room type:Peak cinema, Nights:{nights}, Total cost:${D}"
    elif room_typ1e=="PC":
        return f"Room type:Peak cinema, Nights:{nights}, Total cost:${D}"
    else:
        return "Non valid room type or nights"

@app.route("/services/<fee>")
def bit(fee):
    if fee=="Breakfast":
        return "$0 to get breakfast"
    elif fee=="Laundry":
        return "$0 to wash cloths"
    elif fee=="Airport pickup":
        return "$20 for airport pickup"
    elif fee=="Spa":
        return "$0 for the spa"
    else:
        return "Not valid service"

@app.route("/discount/<customer_type>")
def discount(customer_type):
    if customer_type=="Regular":
        return "5 percent discount"
    elif customer_type=="VIP":
        return "20 percent discount"
    elif customer_type=="Prenium":
        return "10 percent discount"

@app.route("/checkout/<room_type>/<int:nights>/<customer_type")
def checkout(room_type,nights,customer_type):
    B=nights*75
    C=nights*125
    D=nights*175
    if room_type=="business":
        return f"Room type:business, nights:{nights}, Total cost: {B}"
    elif room_type=="business+":
        return f"Room type:business+, nights:{nights}, Total cost: {C}"
    elif room_type=="Peak Cinema":
        return f"Room type:Peak Cinema, nights:{nights}, Total cost: {D}"
    else:
        return "Not valid"

@app.route("/booking/<customer_name>")
def booking(customer_name):
    return f"Booking completed! {customer_name}"


if __name__=="__main__":
    app.run(debug=True) 
