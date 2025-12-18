from flask import Flask, render_template, url_for


app = Flask(__name__)


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