from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # local SQLite file
db = SQLAlchemy(app)


# --- MODELS ---
class Transaction(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # "income" or "expense"
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    note = db.Column(db.String(255))
    
    
    def __repr__(self):
        return f'<Transaction {self.id}>'   
    
    
    
    
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return """MyWallet Pro is a personal finance web application that helps users track their income and expenses, analyze their spending patterns, and visualize financial data through interactive charts. The system provides a clean dashboard, real-time updates, and an intuitive interface to support better financial decision-making."""


if __name__  == "__main__":
    app.run(debug=True)