from flask import Flask, render_template_string, request
import re

app = Flask(__name__)


def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password too short. It should be at least 8 characters long."

    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."

    # Check for a digit
    if not re.search(r'\d', password):
        return "Password should contain at least one digit."

    # Check for a special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."

    return "Password is strong!"


@app.route('/', methods=['GET', 'POST'])
def index():
    strength_message = ""
    if request.method == 'POST':
        password = request.form['password']
        strength_message = check_password_strength(password)
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Strength Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            margin: 0;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        input[type="submit"] {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 1rem;
            padding: 0.75rem;
            border-radius: 4px;
            color: #fff;
        }
        .message.strong {
            background-color: #28a745;
        }
        .message.weak {
            background-color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Password Strength Checker</h1>
        <form method="post">
            <input type="text" name="password" placeholder="Enter your password" required>
            <input type="submit" value="Check Strength">
        </form>
        {% if strength_message %}
            <div class="message {{ 'strong' if 'strong' in strength_message.lower() else 'weak' }}">
                {{ strength_message }}
            </div>
        {% endif %}
    </div>
</body>
</html>
''', strength_message=strength_message)


if __name__ == '__main__':
    app.run(debug=True)
