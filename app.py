from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return """MyWallet Pro is a personal finance web application that helps users track their income and expenses, analyze their spending patterns, and visualize financial data through interactive charts. The system provides a clean dashboard, real-time updates, and an intuitive interface to support better financial decision-making."""


if __name__  == "__main__":
    app.run(debug=True)