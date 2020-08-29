from app import db



class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    books = db.relationship("Book", backref="book", lazy= True)

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = False)
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
    photo_url = db.Column(db.String)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String, nullable=False)
