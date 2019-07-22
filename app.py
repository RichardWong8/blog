from flask import Flask, flash, render_template, request, redirect, url_for, session
from db import *
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register/auth")
def register_auth():
    return

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login/auth")
def login_auth():
    return

@app.route("/logout")
def logout():
    return

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
