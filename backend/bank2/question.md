# Mini Project: Online Banking System (Flask Multiple Routes)

## Objective
Create a Flask application that simulates an online banking system. Use multiple routes, dictionaries, conditional statements, and calculations. No database is required.

---

## Routes to Create

### 1. `/`
Display a welcome message.

---

### 2. `/accounts`
Display all account holders and their account types.

---

### 3. `/account/<username>`
Display:
- Account Holder
- Account Type
- Account Balance
- Account Status

If the account does not exist:
```
Account Not Found
```

---

### 4. `/deposit/<username>/<int:amount>`
Deposit money into the user's account.

Display:
- Previous Balance
- Deposit Amount
- Updated Balance

---

### 5. `/withdraw/<username>/<int:amount>`
Withdraw money from the account.

Rules:
- If balance is sufficient:
  - Display updated balance.
- Otherwise:
```
Insufficient Balance
```

---

### 6. `/transfer/<sender>/<receiver>/<int:amount>`
Transfer money between two accounts.

Requirements:
- Check if both accounts exist.
- Check if sender has sufficient balance.
- Update both balances.

Display:
- Sender
- Receiver
- Amount Transferred
- Updated Balances

---

### 7. `/loan/<username>/<int:salary>/<int:cibil>`
Check loan eligibility.

Rules:
- Salary ≥ ₹40,000
- CIBIL ≥ 750

Display:
- Eligible / Not Eligible
- Maximum Loan Amount (if eligible)

---

### 8. `/statement/<username>`
Generate the account summary.

Display:
- Account Holder
- Account Type
- Current Balance
- Total Deposits
- Total Withdrawals
- Loan Eligibility

---

## Bonus Challenge

Create:

```
/bankreport
```

Display:
- Total Accounts
- Total Bank Balance
- Richest Customer
- Average Account Balance
- Total Loan Eligible Customers

---

## Concepts Practiced

- Multiple Routes
- Route Parameters (`string`, `int`)
- Dictionaries
- Nested Conditional Statements
- Loops
- Mathematical Calculations
- Updating Dictionary Values
- Building a Medium-Sized Flask Application
