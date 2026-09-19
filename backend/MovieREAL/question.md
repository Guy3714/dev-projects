## Objective

Create a simple **Movie Ticket Booking** application using Flask and Jinja templates.

---

## Project Structure

```text
movie_booking/
│
├── app.py
└── templates/
    ├── booking.html
    └── summary.html


---

Route

Create:

/booking

It should support both GET and POST.


---

Booking Form

Create a form with:

1. Customer Name — text input


2. Movie — dropdown:

Avengers

Interstellar

Inception

The Dark Knight



3. Number of Tickets — number input


4. Ticket Type — radio buttons:

Regular — ₹200

Premium — ₹350



5. Snacks — checkbox:

Popcorn & Drink — ₹150



6. Book Tickets button




---

Requirements

When the form is submitted:

Get the values using request.form.

Calculate the ticket cost.

Add ₹150 if snacks are selected.

Calculate the final total.

Display the result using summary.html.


Formula:

Ticket Cost = Ticket Price × Tickets

Total = Ticket Cost + Snack Cost


---

Summary Page

Display:

Movie Booking Summary

Customer: Rahul
Movie: Interstellar
Ticket Type: Premium
Tickets: 2

Ticket Cost: ₹700
Snacks: Yes
Snack Cost: ₹150

Total: ₹850

All values must be dynamic using Jinja.

Example:

<p>Customer: {{ customer }}</p>
<p>Movie: {{ movie }}</p>
<p>Total: ₹{{ total }}</p>


---

Challenge

Add validation:

Maximum 10 tickets

Minimum 1 ticket

Customer name cannot be empty


Bonus

Give a 10% discount when the customer books 5 or more tickets.

Display:

Subtotal
Discount
Final Total


---

Concepts Practiced

Flask routes

GET / POST

HTML forms

request.form

Dropdowns

Radio buttons

Checkboxes

Calculations

Jinja templates

Form validation