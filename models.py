# models.py
from datetime import datetime, date
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # --- Identité ---
    firstname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # --- Infos personnelles ---
    birthdate = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    looking_for = db.Column(db.String(20), nullable=False)

    bio = db.Column(db.Text, default="")
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    # --- Médias ---
    profile_picture = db.Column(db.String(255), default="default.jpg")

    # --- Statut ---
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)

    # --- Dates ---
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    # ---------- MÉTHODES ----------
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )

    def __repr__(self):
        return f"<User {self.firstname} ({self.email})>"
