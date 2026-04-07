#import req packages
from flask import Flask

# Step 1: Create app
app =Flask(__name__)

# Step 2: Create route
@app.route("/")
def Hello():
    return "Hello Jatin"

@app.route("/greet")
def Greet():
    return "Good Evening"

    
@app.route("/add")
def Add():
    a=9
    b=3
    return str(a+b)
# Step 3: Run app
if __name__=="__main__":
    app.run(debug=True)