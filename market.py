from flask import Flask, render_template
app = Flask(__name__) # built in variable.

@app.route("/")
def home_page():
    return render_template('home.html')
