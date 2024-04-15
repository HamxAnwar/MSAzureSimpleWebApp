from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Lenovo IdeaPad Slim", "price": 685.33, "description": "Lenovo IdeaPad Slim 3 15 - Raptor Lake - 13th Gen Core i3 1305u Processor 8-GB 256GB to 2 TB SSD Intel Integrated Graphics 15.6 Full HD 1080p AG Display TPM2.0.", "image": "images/product1.jpeg"},
    {"id": 2, "name": "Samsung Galaxy A15", "price": 162.00, "description": " 6.4-inch SUPER AMOLED capacitive touchscreen display, 90 Hz refresh rate, Mediatek chipset, along with a faster Octa-Core CPU, 6GB of RAM and 128GB of internal memory, 50 MP + 5 MP + 2 MP rear camera sensor and 13 MP selfie camera, massive 5000mAh battery.", "image": "images/product2.jpeg"},
    {"id": 3, "name": "A-110 (Bluetooth Headphone)", "price": 29.99, "description": "Bluetooth & Wired with long battery life.", "image": "images/product3.jpeg"},
    {"id": 4, "name": "Commuter Backpack", "price": 22.97, "description": "Slim shape, Large capacity, Super light.", "image": "images/product4.jpeg"},
    {"id": 5, "name": "Pro Smart Watch", "price": 208.22, "description": "Fitness Tracker, Aluminum Alloy, Weight: 32g, 1.45`` screen, 46x46x10.7mm, 450 mAh battery", "image": "images/product5.jpeg"}
]

# Sample shopping cart data
shopping_cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return "Product not found", 404

@app.route('/cart')
def cart():
    return render_template('cart.html', shopping_cart=shopping_cart)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        shopping_cart.append(product)
        return render_template('index.html', products=products)
    return "Product not found", 404

@app.route('/checkout')
def checkout():
    total = sum(product['price'] for product in shopping_cart)
    return render_template('checkout.html', shopping_cart=shopping_cart, total=total)


if __name__ == '__main__':
    app.run(debug=False)
