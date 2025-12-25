from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash
)
from datetime import datetime
from app.helpers import login_required
from app.extensions import db
from app.models import User, Transaction

main = Blueprint("main", __name__)


def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return db.session.get(User, user_id)


@main.route("/")
@main.route("/home")
@login_required
def dashboard():
    user = get_current_user()

    txs = (
        Transaction.query
        .filter_by(user_id=user.id)
        .order_by(Transaction.date.desc())
        .all()
    )

    total_income = sum(t.amount for t in txs if t.type == "income")
    total_expense = sum(t.amount for t in txs if t.type == "expense")
    balance = total_income - total_expense

    category_summary = {}
    for t in txs:
        if t.type == "expense":
            category_summary[t.category] = category_summary.get(t.category, 0) + t.amount

    return render_template(
        "dashboard.html",
        user=user,
        transactions=txs,
        total_income=total_income,
        total_expense=total_expense,
        balance=balance,
        category_labels=list(category_summary.keys()),
        category_values=list(category_summary.values()),
    )


@main.route("/add", methods=["GET", "POST"])
@login_required
def add_transaction():
    user = get_current_user()

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
        return redirect(url_for("main.dashboard"))

    return render_template("add_transaction.html", user=user)


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            flash("Logged in successfully!", "success")
            return redirect(url_for("main.dashboard"))
        flash("Invalid email or password", "danger")

    return render_template("login.html", user=get_current_user())


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing:
            flash("Username or email already in use", "danger")
            return redirect(url_for("main.register"))

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Account created! Please log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", user=get_current_user())


@main.route("/logout")
@login_required
def logout():
    session.pop("user_id", None)
    flash("Logged out.", "info")
    return redirect(url_for("main.login"))


@main.route("/delete/<int:tx_id>", methods=["POST"])
@login_required
def delete_transaction(tx_id):
    user = get_current_user()

    tx = Transaction.query.get_or_404(tx_id)
    if tx.user_id != user.id:
        flash("Not authorized to delete this transaction.", "danger")
        return redirect(url_for("main.dashboard"))

    db.session.delete(tx)
    db.session.commit()
    flash("Transaction deleted.", "info")
    return redirect(url_for("main.dashboard"))
