from flask import Flask
import random

correct_answer = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def guess_game():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:user_answer>')
def check(user_answer):
    if user_answer < correct_answer:
        return "<h1 style='color: red'>Too Low, Try again!!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif user_answer > correct_answer:
        return "<h1 style='color: purple'>Too High, Try again!!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
