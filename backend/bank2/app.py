from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/accounts")
def holders():
    return "Account holders: David(business), josiph(Climax), john(Suberbs), inder(Business)"

@app.route("/account/<username>")
def account(username):
    if username=="Jatin":
        return "Account holder: Yes, Account type: Suberbian, Account balence: $0, Account status:Certified brokey"
    else:
        return "Not valid account holder"

@app.route("/deposit/<DES>/<int:amount>")
def deposit(DES, amount):
    B=DES+amount
    return f"previous amount:{amount}, Deposit:{DES}, final amount:{B}"

@app.route("/withdraw/<A>/<int:amount>")
def withdraw(A,amount):
    C=amount-A
    return f"Previous amount:{amount}, Withdrawel:{A}, Finak amount:{C}"

@app.route("/loan/<salary>/<cibil>")
def loan(salary, cibil):
    if salary>40000 and cibil>750:
        return "Loan egible!"
    else:
        return "Loan unegible"

