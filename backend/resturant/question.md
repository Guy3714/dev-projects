# 🍽️ Flask Assignment: Restaurant Website (Static Pages)

## 🎯 Objective

Learn how to use `render_template` in Flask to serve **multiple static pages** for a website.

---

## 📌 Task

Build a Flask app for a **Restaurant Website**.

---

## 🛣️ Routes to Create

Create the following routes:

| Route      | Page          |
| ---------- | ------------- |
| `/`        | Home Page     |
| `/menu`    | Menu Page     |
| `/about`   | About Us Page |
| `/contact` | Contact Page  |

---

## 📄 Requirements

### 1. Use `render_template`

Each route should return an HTML page using `render_template()`.

---

### 2. Create HTML files

Inside a `templates` folder, create:

* `home.html`
* `menu.html`
* `about.html`
* `contact.html`

---

### 3. Page Content

Keep it simple:

#### `home.html`

* Restaurant name
* Welcome message

#### `menu.html`

* List of food items (use `<ul>` or `<ol>`)

#### `about.html`

* Short description of the restaurant

#### `contact.html`

* Phone number or email

---

### 4. Navigation (Important ⭐)

Each page must have links to all other pages:

```html id="nav123"
<a href="/">Home</a>
<a href="/menu">Menu</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
```

---

## 🧩 Expected Outcome

* `/` → Home Page
* `/menu` → Menu Page
* `/about` → About Page
* `/contact` → Contact Page

---

## 💡 Hint

```python id="hint456"
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
```

---


## 🏁 Goal

Understand:

* How Flask serves different pages
* How templates are structured
* How a basic website works using Flask
