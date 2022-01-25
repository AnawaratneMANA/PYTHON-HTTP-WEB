from flask import Flask, render_template
app = Flask(__name__) # built in variable.

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '45345345989', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '65398541253', 'price': 600},
        {'id': 3, 'name': 'Keyboard', 'barcode': '98647521654', 'price': 100}
    ]
    return render_template('market.html', items=items)
