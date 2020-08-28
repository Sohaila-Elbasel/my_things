from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SearchForm, Filter, User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dca5f91bd1299c2a4a2db9491840eb05'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://hqethunzcsnxmp:980d9b1b73b638c2eeb2463a40de1885115eacf6d6d484840d876fb6d659c889@ec2-34-238-26-109.compute-1.amazonaws.com:5432/df6alckgo2voap'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

books = [
        {'name': 'Life of Pi',
         'author': 'Yann Martel',
         'published': ' 2003',
         'category': 'action',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/51rxEvLljUL._SX322_BO1,204,203,200_.jpg'
        },
        {'name': 'The Three Musketeers',
         'author': ' Alexandre Dumas',
         'published': '2014',
         'category': 'action',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/41TxXqToCCL._SX348_BO1,204,203,200_.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'classics',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'classics',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'Comic Book',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'horror',
         'img_url': 'https://kbimages1-a.akamaihd.net/fb0c52e7-c427-4eb3-b5aa-9aafc7efea43/353/569/90/False/AhIbw1TJuje1l6QPMtht5A.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'horror',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'horror',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'horror',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'historical',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'historical',
         'img_url': 'https://kbimages1-a.akamaihd.net/fb0c52e7-c427-4eb3-b5aa-9aafc7efea43/353/569/90/False/AhIbw1TJuje1l6QPMtht5A.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'historical',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'fantasy',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'fantasy',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'category': 'fantasy',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },

]

def search(book_name, list):
    result = []
    for book in list:
        if book_name.lower() in book['name'].lower():
            result.append(book)
    return result

@app.route('/', methods=['POST', 'GET'])
def home():
    form = SearchForm()
    if form.search_btn.data:
        result = []
        filters = Filter()
        result = search(form.keywords.data, books)
        return render_template('browse.html', title=form.search_btn.data, form= form, books = result, browse='browse', filters = filters)
    return render_template('home.html', title='Books Store', form= form, books = books[:4])

@app.route('/browse', methods=['POST', 'GET'])
def browse():
    form = SearchForm()
    filters = Filter()

    if filters.go.data:
        filter_list = []
        for book in books:
            if book['category'] == filters.filter.data:
                filter_list.append(book)
        return render_template('browse.html', title=filters.filter.data, form= form, books = filter_list, browse='browse', filters = filters)

    elif form.search_btn.data:
        result = []
        result = search(form.keywords.data, books)
        return render_template('browse.html', title=form.search_btn.data, form= form, books = result, browse='browse', filters = filters)

    return render_template('browse.html', title='Browse Books', form= form, books = books, browse='browse', filters = filters)

@app.route('/books/<string:name>', methods=['POST', 'GET'])
def book(name):
    form = SearchForm()
    return render_template('book.html', title= name, form= form, name= name)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = SearchForm()
    form_register = User()
    if form_register.validate_on_submit():
        flash(f'Acount created for {form_register.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Join Now', form= form, form_register = form_register)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = SearchForm()
    form_register = User()
    if form_register.validate_on_submit():
        flash(f'Acount created for {form_register.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signin.html', title= 'Log in', form= form, form_register = form_register)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
