from .database import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    user_name = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    mybooks = db.relationship("All_books", backref = "creator")

class Sections(db.Model):
    section_id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(100), unique=True, nullable=False)
    s_section_name = db.Column(db.String(100), unique=True, nullable=False)
    pub_date = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    books = db.relationship('All_books', backref='related_section', lazy=True)

class All_books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    s_book_name = db.Column(db.String(100), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.section_id'), nullable=False)
    section = db.relationship('Sections', backref='books_related')
    author = db.Column(db.String(100), nullable=False)
    s_author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    d_link = db.Column(db.String(), nullable=False)

    issue_date = db.Column(db.String(), nullable = True)
    return_date = db.Column(db.String(), nullable = True)
    status = db.Column(db.String(), default = "in store")
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=True)
    user = db.relationship("User", backref="books")

    reviews = db.relationship('Review', backref='book')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('all_books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
