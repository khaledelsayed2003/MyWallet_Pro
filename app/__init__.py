import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask

from app.extensions import db, bcrypt


def create_app():
    app = Flask(__name__)

    # Load .env from /config/.env (same as you already do)
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(BASE_DIR / "config" / ".env")

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-fallback-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///mywallet.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # init extensions
    db.init_app(app)
    bcrypt.init_app(app)

    return app
