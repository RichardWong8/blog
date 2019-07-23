from flask import Flask, flash, render_template, request, redirect, url_for, session
from db import *
import os

app = Flask(__name__)

#app.secret_key = os.urandom(32)

# AUTHENTICATION
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('blog'))

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
            session["username"] = username
            return redirect(url_for("blog"))
        else:
            flash("INCORRECT USERNAME OR PASSWORD")
    return redirect(url_for("login"))

@app.route("/logout", methods=["GET"])
def logout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("home"))

# BLOG RELATED
@app.route("/blog", methods=["GET"])
def blog():
    if not("username" in session):
        return redirect(url_for("login"))

    blog_list = get_blogs(get_user_id(session["username"]))

    return render_template("blog.html", blog_list=blog_list)

@app.route("/blog/create", methods=["GET"])
def create_blog():
    if not("username" in session):
        return redirect(url_for("login"))
    return render_template("create_blog.html")

@app.route("/blog/create/confirm", methods=["POST"])
def create_blog_confirm():
    if not("username" in session):
        return redirect(url_for("login"))
    if request.method == "POST":
        user_id = get_user_id(session["username"])
        blog_title = request.form["blog_title"]
        blog_id = add_blog(user_id, blog_title)
        return redirect(url_for("view_blog", user_id=user_id, blog_id=blog_id))
    return redirect(url_for("create_blog"))

@app.route("/blog/view", methods=["GET"])
def view_blog():
    if not("username" in session):
        return redirect(url_for("login"))
    user_id = request.args["user_id"]
    blog_id = request.args["blog_id"]
    blog_title = get_blog_title(user_id, blog_id)

    session["blog_id"] = blog_id
    session["blog_title"] = blog_title

    entries_list = get_entries(user_id, blog_id)

    return render_template("view_blog.html", blog_title=blog_title, entries_list=entries_list)
@app.route("/entry/create")
def create_entry():
    if not(session["username"] and session["blog_id"]):
        return redirect(url_for("blog"))
    blog_id = session["blog_id"]
    blog_title = session["blog_title"]
    return render_template("create_entry.html", blog_id=blog_id, blog_title=blog_title)

@app.route("/entry/create/confirm", methods=["POST"])
def create_entry_confirm():
    return ""

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.debug = True
    app.run()
