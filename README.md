# MyWallet Pro

**MyWallet Pro** is a personal finance tracking web application built with **Flask**.
It helps users manage income and expenses, visualize spending by category, and track their balance — all with a clean UI and interactive animations.

---

## ✨ Features

- 🔐 **User Authentication**

  - Register / Login / Logout
  - Secure password hashing using **Flask-Bcrypt**
  - Session-based authentication with route protection

- 💸 **Transaction Management**

  - Add income and expense transactions
  - Separate category lists for income & expenses
  - Optional notes per transaction
  - Delete transactions securely

- 📊 **Dashboard & Analytics**

  - Total income, total expenses, and balance summary
  - Pie chart showing expense distribution by category (Chart.js)
  - Recent transactions table

- 🎨 **Modern UI**

  - Bootstrap 5 styling
  - Reusable template components (navbar, transaction table)
  - Animated money GIF on dashboard

- 🐰 **Interactive Rive Animation**

  - Login & Register pages feature a Rive character
  - Character reacts when:

    - Focusing on text inputs
    - Typing password (eyes close)

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Database:** SQLite (via SQLAlchemy ORM)
- **Charts:** Chart.js
- **Animations:** Rive (Canvas runtime)
- **Security:** Flask-Bcrypt, session-based auth
- **Environment Config:** python-dotenv

---

## 📁 Project Structure

```
MyWallet_Pro/
│
├── app/
│   ├── __init__.py        # App factory + config + blueprint registration
│   ├── extensions.py     # SQLAlchemy & Bcrypt instances
│   ├── helpers.py        # login_required decorator
│   ├── models.py         # User & Transaction models
│   ├── routes.py         # All app routes (Blueprint)
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   └── money_anim.gif
│   ├── js/
│   │   ├── charts.js
│   │   ├── category_toggle.js
│   │   ├── rive_login.js
│   │   └── rive_register.js
│   └── rive/
│       └── login_bunny.riv
│
├── templates/
│   ├── components/
│   │   ├── navbar.html
│   │   └── transaction_table.html
│   ├── base.html
│   ├── dashboard.html
│   ├── add_transaction.html
│   ├── login.html
│   └── register.html
│
├── config/
│   ├── .env
│   └── .env.example
│
├── instance/
│   └── mywallet.db
│
├── run.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Environment Setup

Create a `.env` file inside the `config/` folder:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///mywallet.db
```

> Use `.env.example` as a reference.

---

## 🚀 Installation & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/khaledelsayed2003/MyWallet_Pro.git
cd MyWallet_Pro
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
python run.py
```

Open your browser at:

```
http://127.0.0.1:5000
```

---

## 🔐 Authentication Flow

- Users must log in to access dashboard and transactions
- Protected routes use a custom `@login_required` decorator
- Sessions store `user_id`
- Passwords are **hashed**, never stored in plain text

---

## 📊 Charts & Categories

- Expense categories are summarized dynamically
- Chart data is safely passed from Flask → JS using `tojson`
- Category selector switches automatically between income & expense lists

---

## 🎬 Rive Animation Logic

- **Login page**

  - Focus email → character looks attentive
  - Focus password → character closes eyes

- **Register page**

  - Focus username/email → attentive
  - Focus password → eyes close

All animations are handled via **state machine inputs** in `login_bunny.riv`.

---

## 📌 Future Improvements

- Forgot password (email verification)
- Pagination for transactions
- Monthly / yearly reports
- Dark mode
- REST API version

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Built with ❤️ by **Khaled Elsayed**

---
