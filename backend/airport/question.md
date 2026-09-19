# Mini Project: Airport Check-in System (Flask Multiple Routes)

## Objective
Create a Flask application that simulates a simple airport check-in system using multiple routes. No database is required—use hardcoded values.

---

## Routes to Create

### 1. `/`
**Purpose:** Display a welcome message.

**Output:**
```
Welcome to SkyFly Airlines
```

---

### 2. `/flights`
**Purpose:** Display the list of available flights.

**Output:**
```
Available Flights:
- New York
- Los Angeles
- Chicago
- Miami
```

---

### 3. `/flight/<destination>`
**Purpose:** Display flight details.

**Requirements:**
Show:
- Destination
- Departure Time
- Gate Number

If the destination is invalid, display:
```
Flight Not Found
```

---

### 4. `/checkin/<passenger>`
**Purpose:** Check in a passenger.

**Output:**
```
Passenger: John
Check-in Successful
Boarding Pass Generated
```

---

### 5. `/baggage/<int:weight>`
**Purpose:** Calculate baggage charges.

**Rules:**
- Up to 20 kg → No Extra Charge
- 21–30 kg → $50
- Above 30 kg → $100

Display the baggage fee.

---

### 6. `/seat/<seat_type>`
**Purpose:** Display the seat selection fee.

**Seat Prices:**
- Economy → $0
- Premium Economy → $40
- Business → $150
- First Class → $300

If the seat type is invalid, display:
```
Invalid Seat Type
```

---

### 7. `/boarding/<int:minutes>`
**Purpose:** Check boarding status.

**Rules:**
- More than 30 minutes → Boarding Not Started
- 10–30 minutes → Boarding Open
- Less than 10 minutes → Final Call

---

### 8. `/summary/<passenger>/<destination>`
**Purpose:** Display the travel summary.

**Output:**
```
Passenger: John
Destination: Miami
Flight Status: On Time
Gate: A12
```

---

## Bonus Challenge

Create a route:

```
/airport
```

Display:
- Airport Name
- Number of Terminals
- Free Wi-Fi Available
- Lounge Available
- Parking Available

---

## Concepts Practiced

- Multiple Routes
- Route Parameters (`string`, `int`)
- Conditional Statements
- Dictionaries
- Basic Calculations
- Building a Small Flask Application