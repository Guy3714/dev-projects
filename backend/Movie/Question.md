
# 🎬 Flask Mini Project — Movie Dashboard (Jinja Dynamic Page)

## 🎯 Objective

Build a Flask app that displays a dynamic movie dashboard using Jinja variables, loops, and conditions.

---

# 📋 Task

Create a Flask application with a route:

```python
/movies
````

Pass the following data from Flask to HTML:

```python id="2b3u58"
movies = [
    {"name": "Avengers", "rating": 9},
    {"name": "Minecraft Movie", "rating": 7},
    {"name": "Interstellar", "rating": 10},
    {"name": "Cars", "rating": 6}
]
```

---

# 🌐 HTML Page (`movies.html`)

Display:

# 🎥 Movie Dashboard

For every movie show:

* Movie name
* Rating

Example:

```text id="4q2v6v"
🎬 Avengers
⭐ Rating: 9
```

---

# 🔁 Jinja Loop

Use a Jinja `for` loop to display all movies dynamically.

---

# 📁 Folder Structure

```text id="qf5r1f"
project/
│
├── app.py
│
└── templates/
    └── movies.html
```

---

# 🧠 Concepts Practiced

* `render_template()`
* Passing list of dictionaries
* Jinja loops
* Jinja conditions
* Dynamic dashboards
* Accessing dictionary values in Jinja

```
```
