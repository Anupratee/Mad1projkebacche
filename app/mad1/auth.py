from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from mad1.models import db, User

auth = Blueprint("auth", __name__)

@auth.route("/register_sponsor", methods = ["GET", "POST"])
def register_sponsor():
    if request.method == "POST":
        form_name = request.form.get("form_sponsor_name")
        form_email = request.form.get("form_sponsor_email")
        form_password1 = request.form.get("form_sponsor_password1")
        form_password2 = request.form.get("form_sponsor_password2")

        user = User.query.filter_by(email = form_email).first()
        if user:
            flash("Email already registered, please login", category="error")
            return redirect(url_for("auth.login"))
        if form_password1 != form_password2:
            flash("Passwords must be the same", category="error")
            return redirect(url_for("auth.register_sponsor"))
        new_user = User(name = form_name, email = form_email, password = generate_password_hash(form_password1, method="pbkdf2:sha256"), role = "sponsor")
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully", category="success")
        return redirect(url_for("auth.login"))

    return render_template("register_sponsor.html")

@auth.route("/register_influencer", methods = ["GET", "POST"])
def register_influencer():
    return render_template("helloworld.html")

@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        form_email = request.form.get("form_login_email")
        form_password = request.form.get("form_login_password")

        user = User.query.filter_by(email = form_email).first()
        if user:
            if check_password_hash(user.password, form_password):
                login_user(user, remember=True)
                user_id = user.id
                user_role = user.role
                flash("logged in successfully")
                return render_template("helloworld.html")
            else:
                flash("password is wrong")
                return redirect(url_for("auth.login"))
        else:
            flash("create an account")
            return redirect(url_for("auth.register_influencer"))
        
    return render_template("login.html")