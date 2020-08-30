from flask import Flask, session, render_template, url_for, flash, redirect, request
from forms import SearchForm, Filter, UserForm, loginForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dca5f91bd1299c2a4a2db9491840eb05'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://hqethunzcsnxmp:980d9b1b73b638c2eeb2463a40de1885115eacf6d6d484840d876fb6d659c889@ec2-34-238-26-109.compute-1.amazonaws.com:5432/df6alckgo2voap'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    form = SearchForm()
    if form.search_btn.data:
        filters = Filter()
        result = Book.query.filter(Book.name.contains(form.keywords.data))
        return render_template('browse.html', title=f'search for {form.keywords.data}', form= form, books = result, filters = filters)

    books = Book.query.limit(4)
    return render_template('home.html', title='Books Store', form= form, books = books)

@app.route('/browse', methods=['POST', 'GET'])
def browse():
    form = SearchForm()
    filters = Filter()

    if request.method == 'GET':
        books = Book.query.all()

    if filters.go.data:
        filter_list = []
        filter_list = Category.query.get(filters.filter.data).books
        return render_template('browse.html', title=filters.filter.data, form= form, books = filter_list, filters = filters)

    elif form.search_btn.data:
        result = Book.query.filter(Book.name.contains(form.keywords.data))
        return render_template('browse.html', title=f'search for {form.keywords.data}', form= form, books = result, filters = filters)

    return render_template('browse.html', title='Browse Books', form= form, books = books, filters = filters)

@app.route('/books/<int:book_id>/<string:name>', methods=['POST', 'GET'])
def book(book_id, name):
    form = SearchForm()
    book = Book.query.get(book_id)
    category = Category.query.get(book.category_id).name
    return render_template('book.html', title= name, form= form, name= name, book = book, category = category)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SearchForm()
    form_register = UserForm()
    if form_register.validate_on_submit():
        password = generate_password_hash(form_register.password.data)
        user = User(username = form_register.username.data, email = form_register.email.data, password = password)
        db.session.add(user)
        db.session.commit()
        flash(f'Acount created for {form_register.username.data}!', 'success')
        return redirect(url_for('signin'))
    return render_template('register.html', title= 'Join Now', form= form, form_register = form_register)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = SearchForm()
    form_register = loginForm()
    if form_register.validate_on_submit():
        if User.query.filter_by(username = form_register.username.data).first():
            user = User.query.filter_by(username = 'sherif').first()
            if check_password_hash(user.password, form_register.password.data):
                session['username'] = form_register.username.data
                flash(f'{form_register.username.data} has logged in!', 'success')
                return redirect(url_for('home'))
        flash(f'{form_register.username.data} has not logged in!', 'danger')
    return render_template('signin.html', title= 'Log in', form= form, form_register = form_register)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
