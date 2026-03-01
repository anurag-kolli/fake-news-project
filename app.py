from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from news_fetch import fetch_news
from functools import wraps
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this to a secure random key

# Load model and tokenizer
model = load_model("model/fake_news_lstm.h5")
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 300

# Simple user database (in-memory with file backup)
USERS_FILE = "users.json"

def load_users():
    """Load users from file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {
        "admin@example.com": {"password": "admin123", "username": "Admin User"},
        "user@example.com": {"password": "user123", "username": "Test User"}
    }

def save_users(users):
    """Save users to file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

users = load_users()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def predict_fake_news(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN)
    pred = model.predict(padded)[0][0]
    label = "REAL" if pred > 0.5 else "FAKE"
    confidence = pred if pred > 0.5 else 1 - pred
    return label, confidence

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login"""
    error = None
    success = None
    
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        
        # Validate credentials
        if email in users and users[email]["password"] == password:
            session['user_email'] = email
            session['username'] = users[email]["username"]
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)
            return redirect(url_for('index'))
        else:
            error = "Invalid email or password. Please try again."
    
    return render_template("login.html", error=error, success=success)

@app.route("/logout")
def logout():
    """Handle user logout"""
    session.clear()
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    news_results = []
    prediction = None
    confidence = None
    news_text = ""

    if request.method == "POST":
        news_text = request.form.get("news_text", "").strip()
        if news_text:
            prediction, confidence = predict_fake_news(news_text)
    
    # Fetch news with fewer articles for faster loading
    articles = fetch_news("technology", 50)
    for article in articles:
        text = article.get("title", "") + " " + article.get("description", "")
        if text.strip():
            label, conf = predict_fake_news(text)
            article["prediction"] = label
            article["confidence"] = round(conf * 100, 1)
    news_results = articles

    return render_template("index.html", news=news_results, prediction=prediction, confidence=confidence, news_text=news_text)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Handle user signup"""
    global users
    error = None
    success = None
    
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        
        # Validation
        if not username or not email or not password:
            error = "All fields are required."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm_password:
            error = "Passwords do not match."
        elif email in users:
            error = "Email already exists. Please login or use a different email."
        else:
            # Add new user
            users[email] = {
                "password": password,
                "username": username
            }
            save_users(users)
            success = "Account created successfully! Redirecting to login..."
            return redirect(url_for('login'))
    
    return render_template("signup.html", error=error, success=success)

if __name__ == "__main__":
    app.run(debug=True)