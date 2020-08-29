from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo

VALUES = [(1, 'Action and Adventure'), (2, 'Classics'), (3, 'Comic Book'), (4, 'Detective and Mystery'), (5, 'Fantasy'), (6, 'Historical Fiction'), (7, 'Horror'), (8, 'Literary Fiction'), (9, 'Romance'), (10, 'Sci-Fi')]

class SearchForm(FlaskForm):
    keywords = StringField('Keywords', validators=[Length(min=1, max=50)])
    search_btn = SubmitField('Search')

class Filter(FlaskForm):
    filter = SelectField('Filter', choices = VALUES)
    go = SubmitField('Go')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    submit_in = SubmitField('Sign In')

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_in = SubmitField('Sign In')
