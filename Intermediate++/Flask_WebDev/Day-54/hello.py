from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return "<h1>Bye bye my friend</h1>"


@app.route("/<username>")
def greet(username):
    return f"<h1>Greeting Mr/Mrs {username}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
