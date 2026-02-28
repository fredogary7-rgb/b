from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models import User
from flask_jwt_extended import create_access_token
from datetime import datetime

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        birthdate = request.form.get("birthdate")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        gender = request.form.get("gender")
        looking_for = request.form.get("looking_for")
        terms = request.form.get("terms")

        if not all([firstname, birthdate, email, password, confirm_password, gender, looking_for, terms]):
            flash("Tous les champs sont obligatoires.", "danger")
            return redirect(url_for("auth.signup"))

        if password != confirm_password:
            flash("Les mots de passe ne correspondent pas.", "danger")
            return redirect(url_for("auth.signup"))

        if User.query.filter_by(email=email).first():
            flash("Cet email est déjà utilisé.", "warning")
            return redirect(url_for("auth.signup"))

        user = User(
            username=firstname,
            email=email,
            birthdate=datetime.strptime(birthdate, "%Y-%m-%d"),
            gender=gender,
            looking_for=looking_for
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Compte créé avec succès. Connecte-toi.", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash("Email ou mot de passe incorrect.", "danger")
            return redirect(url_for("auth.login"))

        token = create_access_token(identity=user.id)
        return redirect("dashboard.dashboard")

    return render_template("login.html")

