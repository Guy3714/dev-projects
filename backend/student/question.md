# 🏫 Flask Mini Project — Student Marks Dashboard

## 🎯 Objective

Build a Flask app that displays student marks dynamically using Jinja templates.

---

# 📋 Task

Create a Flask application with a route:

```python
/students
```

Pass the following data from Flask to HTML:

```python
students = [
    {"name": "Jatin", "marks": 92},
    {"name": "Rahul", "marks": 67},
    {"name": "Aman", "marks": 45},
    {"name": "Priya", "marks": 81}
]
```

---

# 🌐 HTML Page (`students.html`)

Display:

# 📊 Student Marks Dashboard

For every student show:

- Student name
- Marks

Example:

```text
👨‍🎓 Jatin
📘 Marks: 92
```

---

# 🔁 Jinja Loop

Use a Jinja `for` loop to display all students dynamically.

---

# 📁 Folder Structure

```text
project/
│
├── app.py
│
└── templates/
    └── students.html
```

