from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "37"

@app.route("/bmi/<bmi2>")
def STAT(bmi2):
    bmi2=int(bmi2)
    if bmi2<18.5:
        return "You are underweight"
    elif bmi2>18.5:
        return "Normal weight"
    elif bmi2>29.9:
        return "Overweight"
    else:
        return "Obesity"
    
if __name__=="__main__":
    app.run(debug=True)