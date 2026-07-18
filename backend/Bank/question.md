# Mini Project: Bank Portal (Flask Multiple Routes)

## Objective
Create a Flask application that simulates a simple banking system using multiple routes. No database is required—use hardcoded values.

---

## Routes to Create

### 1. `/`
**Purpose:** Display a welcome message.

**Output:**
```
Welcome to ABC Bank
```

---

### 2. `/balance`
**Purpose:** Display the current account balance.

**Output:**
```
Your current balance is ₹50,000
```

---

### 3. `/deposit/<int:amount>`
**Purpose:** Deposit money into the account.

**Requirements:**
- Assume the initial balance is **₹50,000**.
- Display:
  - Deposited amount
  - Updated balance

**Example:**
```
URL:
/deposit/5000

Output:
Deposited: ₹5000
Updated Balance: ₹55,000
```

---

### 4. `/withdraw/<int:amount>`
**Purpose:** Withdraw money from the account.

**Requirements:**
- If the withdrawal amount is less than or equal to the balance, display the updated balance.
- Otherwise, display:
```
Insufficient Balance
```

---

### 5. `/loan/<int:salary>/<int:cibil>`
**Purpose:** Check loan eligibility.

**Rules:**
- Salary must be **₹30,000 or more**
- CIBIL score must be **750 or above**

**Output:**
```
Loan Approved
```
or
```
Loan Rejected
```

---

### 6. `/fd/<int:amount>/<int:years>`
**Purpose:** Calculate the maturity amount of a Fixed Deposit.

**Formula:**
```
Maturity = Amount + (Amount × 7 × Years / 100)
```

**Example:**
```
URL:
/fd/100000/3

Output:
Principal: ₹100000
Interest: ₹21000
Maturity Amount: ₹121000
```

---

### 7. `/emi/<int:loan>/<int:months>`
**Purpose:** Calculate the monthly EMI.

**Formula:**
```
EMI = Loan Amount / Number of Months
```

**Example:**
```
Loan Amount: ₹600000
Months: 60

Monthly EMI: ₹10000
```

---

### 8. `/account/<name>/<account_type>`
**Purpose:** Display customer details.

**Example:**
```
Name: Harsh
Account Type: Savings
Bank: ABC Bank
```

---

## Bonus Challenge

Create a route:

```
/summary
```

Display:
- Account Holder Name
- Account Number
- Account Type
- Current Balance
- Loan Eligibility
- Fixed Deposit Amount

---
