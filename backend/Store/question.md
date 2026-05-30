# 🛒 Flask Mini Project — Smart Grocery Store

## 🎯 Objective

Practice Flask routes, dynamic URLs, and conditions by building a mini grocery store app.

---

# 📋 Task

Create a Flask app with the following routes:

---

## 🏠 Home Route

```python
/
```

Display:

```text
Welcome to FreshMart Grocery Store
```

---

## 🍎 Product Route

```python
/product/<item>
```

Rules:

- If item is `apple`

```text
Apple costs ₹120 per kg
```

- If item is `milk`

```text
Milk costs ₹60 per packet
```

- If item is `bread`

```text
Bread costs ₹40 per loaf
```

- For any other item:

```text
Sorry, this item is not available
```

---

## 💰 Discount Route

```python
/discount/<int:amount>
```

Rules:

- If amount is greater than 500:

```text
You got 20% discount
```

- If amount is between 200 and 500:

```text
You got 10% discount
```

- Otherwise:

```text
No discount available
```

---

## 🧺 Bill Route

```python
/bill/<item>/<int:qty>
```

Rules:

Use these prices:

| Item | Price |
|---|---|
| apple | 120 |
| milk | 60 |
| bread | 40 |

Calculate:

```text
Total bill for <item> is ₹<total>
```

If item does not exist:

```text
Invalid item selected
```


---

# 🧠 Concepts Practiced

- Flask routes
- Dynamic URL parameters
- Integer converters
- Conditions
- Simple calculations
- String formatting