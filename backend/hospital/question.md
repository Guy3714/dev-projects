# Mini Project: US DMV Portal (Flask Multiple Routes)

## Objective
Create a Flask application that simulates a simple **Department of Motor Vehicles (DMV)** portal in the United States using multiple routes. No database is required—use hardcoded values.

---

## Routes to Create

### 1. `/`
**Purpose:** Display a welcome message.

**Output:**
```
Welcome to the California DMV Portal
```

---

### 2. `/license/<int:age>`
**Purpose:** Check if a person is eligible for a driver's license.

**Rules:**
- Age < 16 → Not Eligible
- Age 16–17 → Learner's Permit Eligible
- Age ≥ 18 → Full Driver's License Eligible

---

### 3. `/registration/<vehicle_type>`
**Purpose:** Display the annual registration fee.

**Fees:**
- Car → $150
- Motorcycle → $75
- Truck → $250

If the vehicle type is invalid, display:
```
Vehicle Type Not Found
```

---

### 4. `/renew/<license_type>`
**Purpose:** Display the renewal fee.

**Fees:**
- Learner Permit → $25
- Standard License → $45
- Commercial License (CDL) → $80

---

### 5. `/speeding/<int:speed_limit>/<int:actual_speed>`
**Purpose:** Check if a speeding ticket should be issued.

**Rules:**
- If the driver exceeds the speed limit, display:
```
Speeding Ticket Issued
Fine: $100
```

Otherwise:
```
No Violation
```

---

### 6. `/parking/<int:hours>`
**Purpose:** Calculate the parking fee.

**Rules:**
- First Hour → Free
- Every Additional Hour → $3

Display the total parking fee.

---

### 7. `/insurance/<vehicle_type>`
**Purpose:** Display the minimum insurance requirement.

**Example:**
- Car → Liability Insurance Required
- Motorcycle → Motorcycle Insurance Required
- Truck → Commercial Insurance Required

---

### 8. `/summary/<name>/<vehicle_type>`
**Purpose:** Display the driver's profile.

**Output:**
```
Driver: John
Vehicle: Car
Registration Status: Active
License Status: Valid
```

---

## Bonus Challenge

Create a route:

```
/office
```

Display:
- DMV Office Hours
- Services Offered
- Walk-ins Available
- Appointment Required (Yes/No)

---

## Concepts Practiced

- Multiple Routes
- Route Parameters (`string`, `int`)
- Conditional Statements
- Basic Calculations
- Building a Small Flask Application