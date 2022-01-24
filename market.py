from flask import Flask
app = Flask(__name__) # built in variable.

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route('/about')
def about_page():
    return "About Text"