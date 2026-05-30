from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Smart City dashboard"

@app.route("/stat/<car>")
def STAT(car):
    car=int(car)
    if car<20:
        return "There is good traffic right now"
    elif  car>50:
        return "Go home little bro"
    else:
        return "There is bad traffic right now"
    

@app.route("/temp/<t>")
def Get_temp(t):
    t=int(t)
    if t>35:
        return "Heat alert"
    elif  t>20:
        return "This is normal weather"
    elif  t<20:
        return "It is very cold"

@app.route("/Level/<level>")
def Get_Level(level):
    level=int(level)
    if level>70:
        return "Heat alert"
    elif  level<20:
        return "It is very cold"
    else:
        return "This is normal weather"

       
@app.route("/power/<unit>")
def Get_Units(unit):
    unit=int(unit)
    if unit>500:
        return "High eltricity usage"
    elif unit>200:
        return "Regular eltricity usage"
    else:
        return "Low eltricity usage"




if __name__=="__main__":
    app.run(debug=True)
