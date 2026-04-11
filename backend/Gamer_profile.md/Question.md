# 🎮 Flask Project: Gamer Profile API

## 🎯 Objective  
Build a Flask backend that simulates a **gamer profile system** using routes.

---

## 🧩 Problem Statement  

You are building a backend for a simple gaming platform.

Create a Flask app with the following routes:

---

## 🕹️ 1. Home Route  

**URL:** `/`  

**Output:**
Welcome to Gamer Hub 🎮

---

## 👤 2. Player Profile (Dynamic Route)  

**URL:** `/player/<username>`  

**Behavior:**
- Display a welcome message for the player  

**Example:**
/player/harsh → Welcome harsh to Gamer Hub 🔥

---

## ❤️ 3. Health Status System  

**URL:** `/health/<int:hp>`  

**Logic:**
- If hp > 70 → "Strong 💪"
- If hp between 30–70 → "In Danger ⚠️"
- If hp < 30 → "Critical 🆘"

**Example:**
/health/80 → Strong 💪  
/health/50 → In Danger ⚠️  
/health/10 → Critical 🆘  

---

## 🧮 4. XP Calculator  

**URL:** `/xp/<int:level>/<int:base>`  

**Logic:**
xp = level * base  

**Example:**
/xp/5/100 → XP is 500  

---

## 🏆 5. Rank System  

**URL:** `/rank/<int:score>`  

**Logic:**
- score > 1000 → "Pro 🏆"
- score > 500 → "Intermediate ⚔️"
- else → "Beginner 🐣"

---