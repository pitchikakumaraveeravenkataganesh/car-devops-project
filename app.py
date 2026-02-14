from flask import Flask, render_template

app = Flask(__name__)

cars_data = [
    {"name": "BMW M4", "price": "₹1.2 Cr", "image": "cars1.jpg"},
    {"name": "Audi R8", "price": "₹2.3 Cr", "image": "cars2.jpg"},
    {"name": "Mercedes AMG", "price": "₹1.8 Cr", "image": "cars3.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cars")
def cars():
    return render_template("cars.html", cars=cars_data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

