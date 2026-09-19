from flask import Flask

app=Flask(__name__)

balance=67

@app.route("/")
def home():
    return "Welcome to the ABC bank"

@app.route("/show_balance")
def show_balance():
    return f"Your bank balence is {balance}"

@app.route("/deposit/<b>")
def deposit(b):
    b=int(b)
    global balance
    balance=balance+b
    return f"Your new bank balence is {balance}"

@app.route("/withdraw/<c>")
def withdraw(c):
    c=int(c)
    global balance
    V=balance-c
    if c>=balance:
        return "Insefficent funds"

    else:
        return f"New bank balence {V}"
    
@app.route("/loan/<A>/<B>")
def loan(A,B):
    A=int(A)
    B=int(B)

    if A>=30000 and B>750:
        return "Loan accepted"
    else:
        return "Loan rejected"

@app.route("/fd/<int:amount>/<int:years>")
def fd(amount,years):
    amount=int(amount)
    years=int(years)

    Ma= amount+(amount*7*years/100)

    return f"{amount},{years},{Ma}"

@app.route("/emi/<int:loan>/<int:month>")
def emi(loan, month):
    EMI=loan/month 
    return f"Your EMI is {EMI}"

@app.route("/account/<name>/<account_type>")
def account(name, account_type):
    return f"Name: {name}, account type:{account_type}, Bank: ABC Bank"

if __name__=="__main__":
    app.run(debug=True)





