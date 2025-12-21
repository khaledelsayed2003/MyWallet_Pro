from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import os


app = Flask(__name__)


# Load the .env file from the config folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / "config" / ".env")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializes: SQLAlchemy: for database operations (ORM - Object Relational Mapping), Bcrypt: for password hashing/encryption
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# --- MODELS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password: str):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)
    
    transactions = db.relationship(
    "Transaction",
    backref="user",
    lazy=True,
    cascade="all, delete"
    )
    

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # income / expense
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    note = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    



# --- HELPERS ---
def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return User.query.get(user_id)




@app.route('/home')
@app.route("/")
def home():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        user=user,
        transactions=[],
        total_income=0,
        total_expense=0,
        balance=0,
        category_labels=[],
        category_values=[],
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            flash("Logged in successfully!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Check duplicates
        existing = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing:
            flash("Username or email already in use", "danger")
            return redirect(url_for("register"))

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out.", "info")
    return redirect(url_for("login"))


@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = float(request.form.get("amount"))
        t_type = request.form.get("type")
        category = request.form.get("category")
        date_str = request.form.get("date")
        note = request.form.get("note") or ""

        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        else:
            date = datetime.utcnow()

        tx = Transaction(
            amount=amount,
            type=t_type,
            category=category,
            date=date,
            note=note,
            user_id=user.id,
        )

        db.session.add(tx)
        db.session.commit()

        flash("Transaction added successfully!", "success")
        return redirect(url_for("home"))

    return render_template("add_transaction.html", user=user)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()  #only creates if doesn't exist
    app.run(debug=True)