# Fake News Detection Dashboard

A modern, stylish web application for detecting fake news using LSTM neural networks.

## Features

✨ **Stylish Login System**
- Modern, gradient-based design with animations
- Email and password authentication
- Remember me functionality
- Password recovery (placeholder)
- User profile integration

🎨 **Dashboard**
- Real-time news article analysis
- Fake/Real classification with confidence scores
- Manual news text verification
- Latest news feed integration
- User-friendly interface with logout functionality

🤖 **AI Detection**
- LSTM-based fake news detection model
- High accuracy predictions
- Confidence percentage display
- Pre-trained model support

## Setup Instructions

### 1. **Prerequisites**
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### 2. **Installation**

```bash
# Navigate to the project directory
cd fake_news_app

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install flask tensorflow keras numpy scikit-learn pickle
```

### 3. **Run the Application**

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Default Login Credentials

Use these credentials to access the dashboard:

### Admin Account
- **Email:** `admin@example.com`
- **Password:** `admin123`

### Test Account
- **Email:** `user@example.com`
- **Password:** `user123`

## Creating a New Account

1. Click "Sign up here" on the login page
2. Enter your full name, email, and password
3. Password requirements:
   - Minimum 6 characters
   - At least one uppercase letter
   - At least one number
4. Confirm your password and submit

## File Structure

```
fake_news_app/
├── app.py                 # Main Flask application
├── login.html            # Login page template
├── signup.html           # Signup page template
├── index.html            # Dashboard template
├── users.json            # User database (auto-generated)
├── news_fetch.py         # News fetching module
├── train_lstm.py         # Model training script
├── Fake.csv              # Fake news dataset
├── True.csv              # Real news dataset
└── model/
    ├── fake_news_lstm.h5 # Pre-trained model
    └── tokenizer.pkl     # Tokenizer for preprocessing
```

## Usage Guide

### Logging In
1. Go to `http://localhost:5000`
2. Enter your email and password
3. Check "Remember me" to stay logged in
4. Click "Sign In"

### Checking News Articles
1. Navigate to the dashboard
2. Paste news text in the checking section
3. Click "Check News"
4. View the prediction (FAKE/REAL) and confidence percentage

### Viewing Latest News
1. The dashboard displays latest technology news
2. Each article shows:
   - Article title and description
   - Prediction badge (FAKE/REAL)
   - Confidence percentage

### Logging Out
1. Click your user avatar in the top-right
2. Click the "Logout" button

## Customization

### Change Secret Key
In `app.py`, update the secret key for production:
```python
app.secret_key = 'your-secure-random-key-here'
```

### Modify News Category
In `app.py`, change the news fetch category:
```python
articles = fetch_news("politics", 10)  # Change "technology" to your category
```

### Adjust Model Sensitivity
In `app.py`, modify the prediction threshold:
```python
label = "REAL" if pred > 0.5 else "FAKE"  # Adjust 0.5 threshold
```

## Security Notes

⚠️ **Important**: This is a demonstration application.

For production deployment:
1. Use a secure secret key
2. Implement password hashing (bcrypt)
3. Add HTTPS/SSL
4. Use a proper database (PostgreSQL, MongoDB)
5. Implement rate limiting
6. Add CSRF protection
7. Implement proper session management

## Troubleshooting

### "Model not found" error
- Ensure `fake_news_lstm.h5` is in the `model/` folder
- Ensure `tokenizer.pkl` is in the `model/` folder

### Login page not loading
- Check if Flask is installed: `pip install flask`
- Verify the templates folder exists and contains HTML files

### News not showing
- Check your internet connection
- Verify the news API is working
- Check `news_fetch.py` configuration

### Port already in use
```bash
# Change the port in app.py:
app.run(debug=True, port=5001)
```

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Database:** JSON (can be upgraded to MongoDB/PostgreSQL)
- **ML Model:** TensorFlow/Keras (LSTM)
- **Frontend:** HTML5, CSS3 (with modern animations)
- **Authentication:** Flask sessions

## Project Structure Overview

```
Fake News Detection ↓
├── User Authentication
│   ├── Login
│   ├── Signup
│   └── Session Management
├── News Analysis
│   ├── Manual Text Input
│   ├── Automated Feed Processing
│   └── LSTM Model Prediction
└── Dashboard
    ├── User Profile
    ├── News Display
    └── Prediction Results
```

## Future Enhancements

- [ ] Social media login integration
- [ ] Advanced analytics dashboard
- [ ] Model explanation (LIME/SHAP)
- [ ] Browser extension
- [ ] Mobile app
- [ ] Real-time notifications
- [ ] Multi-language support
- [ ] Dark mode theme

## Support

For issues or questions, please check the code comments or contact support.

---

**Made with ❤️ for Fake News Detection**
