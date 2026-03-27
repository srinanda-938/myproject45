
from flask import Flask, render_template, request

app = Flask(__name__)

def suggest_price(price, demand, stock):
    price = float(price)
    stock = int(stock)

    # Demand logic
    if demand == "High":
        price *= 1.10
    elif demand == "Low":
        price *= 0.90

    # Stock logic
    if stock > 100:
        price *= 0.95
    elif stock < 20:
        price *= 1.05

    return round(price, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        price = request.form["price"]
        demand = request.form["demand"]
        stock = request.form["stock"]

        result = suggest_price(price, demand, stock)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)