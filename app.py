from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
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


@app.route('/')
@app.route('/home')
def home():
    return render_template(
        "dashboard.html",
        user=None,
        transactions=[],
        total_income=0,
        total_expense=0,
        balance=0,
        category_labels=[],
        category_values=[],
    )

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/add")
def add_transaction():
    return render_template("add_transaction.html")


if __name__  == "__main__":
    app.run(debug=True)