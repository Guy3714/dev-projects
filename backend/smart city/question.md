# 🧠 Flask Project: Smart City Control System

## 🎯 Objective  
Build a Flask backend that simulates a **smart city dashboard** using routes and logic.

---

## 🧩 Problem Statement  

You are building a backend for a **Smart City System** that monitors different services.

Create a Flask app with the following routes:

---

## 🌆 1. Home Route  

**URL:** `/`  

**Output:**  
Smart City Dashboard 🏙️  

---

## 🚦 2. Traffic Status  

**URL:** `/traffic/<int:cars>`  

**Logic:**  
- cars < 20 → "Smooth Traffic 🟢"  
- cars between 20–50 → "Moderate Traffic 🟡"  
- cars > 50 → "Heavy Traffic 🔴"  

**Example:**  
/traffic/10 → Smooth Traffic 🟢  
/traffic/35 → Moderate Traffic 🟡  
/traffic/80 → Heavy Traffic 🔴  

---

## 🌡️ 3. Weather Alert  

**URL:** `/weather/<int:temp>`  

**Logic:**  
- temp > 35 → "Heat Alert 🔥"  
- temp between 20–35 → "Normal Weather ☀️"  
- temp < 20 → "Cold Weather ❄️"  

---

## 💧 4. Water Tank Monitor  

**URL:** `/water/<int:level>`  

**Logic:**  
- level > 70 → "Water Full 💧"  
- level between 30–70 → "Water Moderate 🚿"  
- level < 30 → "Water Low ⚠️"  

---

## ⚡ 5. Electricity Usage  

**URL:** `/power/<int:units>`  

**Logic:**  
- units > 500 → "High Usage ⚡"  
- units > 200 → "Normal Usage 🔌"  
- else → "Low Usage 💡"  

---

## 🛠 Requirements  

- Use Flask  
- Minimum **5 routes**  
- Use **dynamic routing**  
- Apply **if-else logic**  

---
