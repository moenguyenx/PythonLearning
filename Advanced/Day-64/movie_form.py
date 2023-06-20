from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # year = IntegerField("Year", validators=[DataRequired()])
    # description = StringField("Description", validators=[DataRequired()])
    # rating = FloatField("Rating", validators=[DataRequired()])
    # ranking = IntegerField("Ranking", validators=[DataRequired()])
    # review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField('Submit')