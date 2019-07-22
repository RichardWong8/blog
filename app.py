from flask import Flask, flash, render_template, request, redirect, url_for, session
from db import *
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/register/auth", methods=["POST"])
def register_auth():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        if get_user_id(username) == -1:
            if password == confirm:
                add_user(username, password)
                flash("ACCOUNT SUCCESSFULLY CREATED")
            else:
                flash("PASSWORDS DO NOT MATCH")
        else:
            flash("USERNAME TAKEN")
    return redirect(url_for("register"))

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/login/auth", methods=["POST"])
def login_auth():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate_user(username, password):
            return redirect(url_for("blog"))
        else:
            flash("INCORRECT USERNAME OR PASSWORD")
    return redirect(url_for("login"))

@app.route("/blog")
def blog():
    return

@app.route("/logout")
def logout():
    return

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
