from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def life():
    return "Least favorite project ever!"

@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        customer = request.form.get("customer_name", "").strip()
        movie = request.form.get("movie")
        ticket_type = request.form.get("ticket_type")
        tickets = int(request.form.get("tickets", 0))

        prices = {"Regular": 200, "Premium": 350}
        ticket_cost = prices[ticket_type] * tickets
        snacks_selected = request.form.get("snacks") is not None
        snack_cost = 150 if snacks_selected else 0
        total = ticket_cost + snack_cost

        return render_template(
            "summary.html",
            customer=customer,
            movie=movie,
            ticket_type=ticket_type,
            tickets=tickets,
            ticket_cost=ticket_cost,
            snacks="Yes" if snacks_selected else "No",
            snack_cost=snack_cost,
            total=total,
        )

    return render_template("booking.html")

if __name__ == "__main__":
    app.run(debug=True)