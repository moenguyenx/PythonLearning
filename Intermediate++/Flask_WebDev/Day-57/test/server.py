from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 9)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=year)


@app.route("/guess/<string:name>")
def guess_gender(name):
    parameter = {
        "name": name
    }
    response = requests.get(url="https://api.genderize.io/", params=parameter)
    gender = response.json()["gender"]
    return render_template("guess.html", my_name=name, guess=gender)


@app.route("/blog")
def get_blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)