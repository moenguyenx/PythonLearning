from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

now = datetime.now()
MY_EMAIL = "qminh1908@gmail.com"
PASSWORD = "gvosjbtnqjvaauwq"

data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=data, now=now)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_input = request.form
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="minh.nq214010@sis.hust.edu.vn",
                                msg=f"Subject: Form Submission\n\n"
                                    f"Name: {user_input['name']}\n"
                                    f"Phone Number: {user_input['phone']}\n"
                                    f"Email: {user_input['email']}\n"
                                    f"Message: {user_input['message']}")
        return render_template("contact.html")
    return render_template("contact.html")


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for item in data:
        if item["id"] == index:
            requested_post = item
    return render_template("post.html", post=requested_post, now=now)


if __name__ == "__main__":
    app.run(debug=True)
