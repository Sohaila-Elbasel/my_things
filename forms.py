from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo

VALUES = [('action', 'Action and Adventure'), ('classics', 'Classics'), ('comic', 'Comic Book'), ('mystery', 'Detective and Mystery'), ('fantasy', 'Fantasy'), ('historical', 'Historical Fiction'), ('horror', 'Horror'), ('fiction', 'Literary Fiction'), ('romance', 'Romance'), ('sci-fi', 'Sci-Fi')]

class SearchForm(FlaskForm):
    keywords = StringField('Keywords', validators=[Length(min=1, max=50)])
    search_btn = SubmitField('Search')

class Filter(FlaskForm):
    filter = SelectField('Filter', choices = VALUES)
    go = SubmitField('Go')

class User(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    submit_in = SubmitField('Sign In')
