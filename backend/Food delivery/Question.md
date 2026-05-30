# 🍔 Flask Project: Food Delivery Backend

## 🎯 Objective  
Build a Flask backend that simulates a **food delivery system** using routes and logic.

---

## 🧩 Problem Statement  

You are building a backend for a **food delivery app**.

Create a Flask app with the following routes:

---

## 🏠 1. Home Route  

**URL:** `/`  

**Output:**  
Welcome to FoodExpress 🍔  

---

## 📋 2. Menu Item  

**URL:** `/menu/<item>`  

**Behavior:**  
Return a message like:  
You ordered <item> 😋  

**Example:**  
/menu/pizza → You ordered pizza 😋  

---

## 🚚 3. Delivery Time Estimator  

**URL:** `/delivery/<int:distance>`  

**Logic:**  
- distance < 5 → "Delivery in 10 mins 🕒"  
- distance between 5–15 → "Delivery in 30 mins 🚴"  
- distance > 15 → "Delivery in 60 mins 🚗"  

---

## 💰 4. Bill Calculator  

**URL:** `/bill/<int:amount>`  

**Logic:**  
- amount > 1000 → "Discount Applied 🎉 Final: amount - 200"  
- amount > 500 → "Discount Applied 🎉 Final: amount - 100"  
- else → "No Discount ❌ Final: amount"  

👉 Replace `amount` with calculated value  

---

## ⭐ 5. Order Status  

**URL:** `/status/<status>`  

**Logic:**  
- preparing → "Your food is being prepared 👨‍🍳"  
- out → "Out for delivery 🚚"  
- delivered → "Delivered! Enjoy your meal 😍"  
- else → "Invalid status ❓"  

---

## 🛠 Requirements  

- Use Flask  
- At least **5 routes**  
- Use **dynamic parameters**  
- Use **if-else logic**  

---
