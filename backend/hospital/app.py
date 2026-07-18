from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to California DMV portal"

@app.route("/liscence/<int:age>")
def liscence(age):
    if age<16:
        return "Not egiable"

    elif age>16:
        return "Learners permit"

    elif age>18:
        return "Able to get a full drivers liscence"

    else:
        return "Not valid"

@app.route("/registration/int:<vehicle>")
def registration(vehicle):
    if vehicle==car:
        return "Your fee for registration is $150"
    elif vehicle==motorcycle:
        return "Your fee for registration is $75"
    elif vehicle==truck:
        return "Your fee for registration is $250"
    else:
        return "Invalid vehicle type"

@app.route("/renew/<liscence_type>")
def renew(liscence_type):
    if liscence_type==learners_permit:
        return "Fee to renew a learners_permit is $25"

    elif liscence_type==regular:
        return "Fee for regular liscence $45"

    elif liscence_type==CDL:
        return "Fee for a CDL liscence is $80"
    else:
        return "That liscence type does not exist"
    
@app.route("/speeding/<int:speeding_limit>/<int:actul_speed>")
def speeding(speeding_limit,actul_speed):
    if actul_speed>=speeding_limit:
        return "You have a $100 speeding ticket"
    else:
        "No speeding ticket"

@app.route("/parking/<int:hours>")
def parking(hours):
    return hours*3-3


@app.route("/insurance/int:<vehicle1>")
def insurance(vehicle1):
    if vehicle1==car:
        return "At least Liability isurance needed"
    elif vehicle1==motorcycle:
        return "motorcycle insurance needed"
    elif vehicle1==truck:
        return "Comerical insurance required"
    else:
        return "Invalid vehicle type"

@app.route("/summary/<name>/<vehicle_type")
def summary(name,vehcile_type):
    return f"name:{name}, vehicle type:{vehcile_type}, Liscence:Aquired, Liscence Status: Valid"

if __name__=="__main__":
    app.run(debug=True) 