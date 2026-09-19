# Mini Project: Hotel Reservation System (Flask Multiple Routes)

## Objective
Create a Flask application that simulates a hotel reservation system using multiple routes. No database is required. Use dictionaries, conditional statements, and calculations.

---

## Routes to Create

### 1. `/`
Display a welcome message.

---

### 2. `/rooms`
Display all available room types and their price per night.

---

### 3. `/room/<room_type>`
Display:
- Room Type
- Price per Night
- Maximum Occupancy
- Availability

If the room type does not exist:
```
Room Not Found
```

---

### 4. `/book/<room_type>/<int:nights>`
Calculate the room booking cost.

Display:
- Room Type
- Nights
- Total Cost

---

### 5. `/services/<service>`
Display the service charge.

Services:
- Breakfast
- Laundry
- Airport Pickup
- Spa

---

### 6. `/discount/<customer_type>/<int:bill>`
Apply discount based on customer type.

- Regular → 5%
- Premium → 10%
- VIP → 20%

---

### 7. `/checkout/<room_type>/<int:nights>/<customer_type>`
Generate the final bill.

Display:
- Room Cost
- Discount
- GST (18%)
- Final Amount

---

### 8. `/booking/<customer_name>`
Display the booking summary.

---

## Bonus Challenge

Create:

```
/summary
```

Display:
- Total Room Types
- Cheapest Room
- Most Expensive Room
- Hotel Rating

---

## Concepts Practiced

- Multiple Routes
- Dictionaries
- Route Parameters
- Nested Conditions
- Calculations
- Reusing Data
