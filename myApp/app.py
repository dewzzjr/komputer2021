from flask import Flask, render_template
import query

# https://flask.palletsprojects.com/en/2.0.x/installation/
# > mkdir myApp
# > cd myApp
# > py -3 -m venv venv
# > venv\Scripts\activate
# > pip install Flask
# > set FLASK_APP=hello

app = Flask(__name__)

# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# > venv\Scripts\activate
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

# HALAMAN USER HTML
# menampilkan daftar user yang ada di table users
@app.route("/users")
def all_user_page():
    users = query.getall()
    # print(users)
    return render_template("users.html", data=users)