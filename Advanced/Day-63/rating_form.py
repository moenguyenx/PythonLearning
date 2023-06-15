from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RatingForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')