from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.relationship("Category", backref="book", lazy=True)
    name = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float(5), nullable=False)
    rate = db.Column(db.Float(3))
    height = db.Column(db.Float(5))
    width = db.Column(db.Float(5))
    depth = db.Column(db.Float(5))
    weight = db.Column(db.Float(5))
    author = db.Column(db.String(50), nullable=False)
    published = db.Column(db.DateTime())
    summary = db.Column(db.String(), nullable=False)
    about_author = db.Column(db.String())
    age_range = db.Column(db.String(5))
    pages = db.Column(db.String(5))
    publisher = db.Column(db.String(50))
    language = db.Column(db.String(20))
    condition = db.Column(db.String(25))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(), primary_key = True)
