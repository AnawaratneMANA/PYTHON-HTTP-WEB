from flask import Flask
app = Flask(__name__) # built in variable.

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the dynamic Route {username}</h1>'