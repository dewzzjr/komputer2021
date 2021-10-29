from flask import Flask, render_template

# https://flask.palletsprojects.com/en/2.0.x/installation/
# > mkdir myproject
# > cd myproject
# > py -3 -m venv venv
# > venv\Scripts\activate
# > pip install Flask

app = Flask(__name__)

# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# > set FLASK_APP=hello
# > flask run

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <a href='/hello'>Click Here</a>"

@app.route("/hello")
def hello_dewangga():
    return "<p>Hello, Dewangga!</p>"

@app.route("/hello/<username>")
def hello_user(username):
    greeting = "Selamat Datang"
    return f"<p>{greeting}</p><p>Hello, {username}!</p>"

@app.route("/user/<name>")
def user_page(name=None):
    return render_template("hello.html", name=name)

@app.route("/input", methods=['POST'])
def input():
    return render_template("input.html")