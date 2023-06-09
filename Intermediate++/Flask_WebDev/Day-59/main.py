from flask import Flask, render_template
import requests
from datetime import datetime

now = datetime.now()
data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=data, now=now)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
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
