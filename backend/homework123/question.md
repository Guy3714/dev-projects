# Mini Project: Amazon Order Tracking System (Flask Multiple Routes)

## Objective
Create a Flask application that simulates a simple Amazon order tracking system using multiple routes. No database is required—use hardcoded values.

---

## Routes to Create

### 1. `/`
**Purpose:** Display a welcome message.

**Output:**
```
Welcome to Amazon Order Tracking Portal
```

---

### 2. `/orders`
**Purpose:** Display a list of recent orders.

**Output:**
```
Recent Orders:
- Echo Dot
- Fire TV Stick
- Apple AirPods
- Kindle Paperwhite
```

---

### 3. `/order/<order_id>`
**Purpose:** Display the order details.

**Requirements:**
Show:
- Product Name
- Order Date
- Order Status

If the order ID is invalid, display:
```
Order Not Found
```

---

### 4. `/track/<order_id>`
**Purpose:** Display the shipping status.

**Possible Statuses:**
- Ordered
- Packed
- Shipped
- Out for Delivery
- Delivered

---

### 5. `/shipping/<state>`
**Purpose:** Display the shipping cost.

**Rules:**
- California → $10
- Texas → $8
- Florida → $12
- New York → $15

If shipping is unavailable:
```
Shipping Not Available
```

---

### 6. `/delivery/<int:days>`
**Purpose:** Display the delivery type.

**Rules:**
- 1 Day → Same Day Delivery
- 2 Days → Prime Delivery
- 3–5 Days → Standard Delivery
- More than 5 Days → Economy Delivery

---

### 7. `/return/<order_id>/<int:days>`
**Purpose:** Check return eligibility.

**Rules:**
- Returned within 30 days → Return Accepted
- More than 30 days → Return Rejected

---

### 8. `/invoice/<order_id>/<int:amount>`
**Purpose:** Generate an invoice.

Display:
- Order ID
- Product Price
- Tax (8%)
- Final Amount

---