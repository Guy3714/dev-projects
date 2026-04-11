from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the gaming website"

# localhost:3000/player/jatin
@app.route("/player/<username>")
def player(username):
    return f"Welcome to the gaming website. {username}"

@app.route("/stat/<hp>")
def STAT(hp):
    hp=int(hp)
    if hp>70:
        return f"You are healthy at {hp}"
    elif hp<70:
        return f"You are unhealthy at {hp}"
    elif  hp<10:
        return f"YOU ARE DIEING SEEK SHELTER LITTLE BRO"

            

@app.route("/XP/<level>/<base>")
def Xp(level,base):
    level= int(level)
    base= int(base)
    xp=level * base
    return f"XP is {xp}"

@app.route("/rank/<int:score>")
def Score(score):
    score=int(score)
    if score>500:
        return "WOW A PRO GAMER"
    elif  score>300:
        return "You are a intermidate player"
    elif  score<100:
        return "YOU SUCK AT THIS GAME"
    

if __name__=="__main__":
    app.run(debug=True)
