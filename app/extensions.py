from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initializes: SQLAlchemy: for database operations (ORM - Object Relational Mapping), Bcrypt: for password hashing/encryption
db = SQLAlchemy()
bcrypt = Bcrypt()