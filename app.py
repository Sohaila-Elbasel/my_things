from flask import Flask, render_template, url_for, flash, redirect
from forms import SearchForm, Filter, User
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dca5f91bd1299c2a4a2db9491840eb05'
engine = create_engine('postgres://hqethunzcsnxmp:980d9b1b73b638c2eeb2463a40de1885115eacf6d6d484840d876fb6d659c889@ec2-34-238-26-109.compute-1.amazonaws.com:5432/df6alckgo2voap')

books = [
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/fb0c52e7-c427-4eb3-b5aa-9aafc7efea43/353/569/90/False/AhIbw1TJuje1l6QPMtht5A.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/fb0c52e7-c427-4eb3-b5aa-9aafc7efea43/353/569/90/False/AhIbw1TJuje1l6QPMtht5A.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/fb0c52e7-c427-4eb3-b5aa-9aafc7efea43/353/569/90/False/AhIbw1TJuje1l6QPMtht5A.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://images-na.ssl-images-amazon.com/images/I/81WunXo0giL.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },
        {'name': '1984',
         'author': 'George Orwell',
         'published': '1949',
         'img_url': 'https://kbimages1-a.akamaihd.net/e39ed975-600f-49c7-b29d-5d531f24f09f/353/569/90/False/dSCAQLyKPDObZmRnq4PCYQ.jpg'
        },

]

@app.route('/', methods=['POST', 'GET'])
def home():
    form = SearchForm()
    return render_template('home.html', title='Books Store', form= form, books = books[:4])

@app.route('/browse', methods=['POST', 'GET'])
def browse():
    form = SearchForm()
    filters = Filter()
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
