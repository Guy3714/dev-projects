# Login App (Flask)

## Project Structure
```
login_app/
│
├── app.py
└── templates/
    └── login.html
```

## `app.py`
```python
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Required for using sessions
app.secret_key = "my-secret-key"


@app.route("/")
def home():
    if "username" in session:
        return f"Welcome, {session['username']}!"

    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Temporary hardcoded credentials
        if username == "admin" and password == "1234":

            session["username"] = username

            return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
```

## `templates/login.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>

<body>

    <h1>Login</h1>

    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    <form method="POST">

        <label>Username:</label>
        <input type="text" name="username" required>

        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>

        <br><br>

        <button type="submit">Login</button>

    </form>

</body>
</html>
```

## How It Works

1. **Opening `/login`** — Flask displays the login template.
2. **Submitting the form** with `username = admin`, `password = 1234`:
   ```python
   if username == "admin" and password == "1234":
   ```
3. **If correct:**
   ```python
   session["username"] = username
   ```
   The username is stored in the session, and the user is redirected to `/`.
4. **If incorrect**, Jinja displays the error:
   ```html
   {% if error %}
       <p>{{ error }}</p>
   {% endif %}
   ```
5. **The `/logout` route** removes the session:
   ```python
   session.pop("username", None)
   ```

## Try These Credentials

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `1234` |
```