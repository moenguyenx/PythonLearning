from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)

app.secret_key = "vlluondaucatmoi"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print("Form data:", form.data)
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        print("Form errors:", form.errors)
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
