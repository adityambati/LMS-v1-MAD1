from flask import Flask, render_template, redirect, request
from flask import current_app as app
from datetime import datetime
from .models import *


admin_data = [
    {"a_name": "admin", "pwd": "12345"}
]


@app.route('/admin_login', methods = ['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        a_name = request.form.get("admin_name")
        pwd = request.form.get("pwd")
        for data in admin_data:
            if data["a_name"] == a_name:
                if data["pwd"] == pwd:
                    return redirect('/admin')
                else:
                    return "wrong pass"
            else:
                return "u dont exist lol"
    return render_template('admin_login.html')

@app.route('/', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(user_name = username).first()
        if this_user:
            if this_user.password == pwd:
                return redirect(f'/user/{this_user.id}')
            else:
                return "wrong pass"
        else:
            return "u dont exist lol"
    return render_template('user_login.html')

@app.route('/register', methods = ['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get("username")
        pwd1 = request.form.get("pwd1")
        pwd2 = request.form.get("pwd2")
        this_user = User.query.filter_by(user_name = username).first()
        if this_user:
            return "user already exists"
        else:
            if (pwd1 == pwd2):
                new_user = User(user_name = username, password = pwd1)
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            else:
                return "check ur pass"
    return render_template('register.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin_dash():
    sec = Sections.query.all()
    print(sec)
    return render_template('admin_dash_sec.html', sec =sec)

@app.route('/user/<int:user_id>', methods = ['GET', 'POST'])
def user_dash(user_id):
    user = User.query.get(user_id)
    my_books = user.mybooks
    return render_template('user_dash_mybooks.html', u_id = user.id, u_name = user.user_name, my_books = my_books)

@app.route('/user_dash_allbooks/<int:user_id>', methods = ['GET', 'POST'])
def all_books(user_id):
    books = All_books.query.filter_by(status='in store').all()
    user = User.query.get(user_id)
    print(books)
    return render_template('user_dash_allbooks.html', u_id = user.id, u_name = user.user_name, books = books)

@app.route('/book_manage', methods = ['GET', 'POST'])
def book_manage():
    book_apr = All_books.query.filter_by(status='with the admin').all()
    book_given = All_books.query.filter_by(status='with user').all()
    return render_template('book_manage.html', book_apr = book_apr, book_given = book_given)

@app.route('/add_sec', methods = ['GET', 'POST'])
def add_sec():
    if request.method == 'POST':
        section_name = request.form.get('s_name')
        pub_date = request.form.get('date0')
        description = request.form.get('description')
        new_sec = Sections(section_name = section_name, s_section_name = raw(section_name), pub_date = pub_date, description = description)
        print(new_sec)
        print(pub_date)
        db.session.add(new_sec)
        db.session.commit()
        return redirect('/admin')
    return render_template('add_sec.html')

@app.route('/del_sec', methods = ['GET', 'POST'])
def del_sec():
    if request.method == "POST":
        s_name = request.form.get('s_name')
        sec = Sections.query.filter_by(section_name = s_name).first()
        print(sec)
        associated_books = All_books.query.filter_by(section_id=sec.section_id).all()
        for book in associated_books:
            db.session.delete(book)
            db.session.commit()
        db.session.delete(sec)
        db.session.commit()
        return redirect('/admin')
    return render_template('del_sec.html')

@app.route('/del_book', methods = ['GET', 'POST'])
def del_book():
    if request.method == "POST":
        b_name = request.form.get('b_name')
        book = All_books.query.filter_by(book_name = b_name).first()
        print(book)
        db.session.delete(book)
        db.session.commit()
        return redirect('/admin')
    return render_template('del_book.html')

@app.route('/books_of_sec/<int:sec_id>', methods = ['GET', 'POST'])
def books_of_sec(sec_id):
    this_sec = Sections.query.get(sec_id)
    books_in_sec = this_sec.books
    return render_template('books_of_sec.html', sec_id=sec_id, books=books_in_sec)

@app.route('/add_book', methods = ['GET', 'POST'])
def add_book():
        if request.method == 'GET':
            sections = Sections.query.all()
            return render_template('add_book.html',  sections = sections)
        elif request.method == 'POST':
            book_name = request.form.get('b_name')
            author = request.form.get('a_name')
            d_link = request.form.get('d_link')
            date_str = request.form.get('date1')
            sec_name = request.form.get('sec_book')
            content = request.form.get('content')
            published_date = datetime.strptime(date_str,'%Y-%m-%d').date()
            section = Sections.query.filter_by(section_name=sec_name).first()
            if section:
                new_book = All_books(book_name = book_name, s_book_name = raw(book_name), section_id = section.section_id, author = author, s_author = raw(author), d_link = d_link, published_date = published_date, content = content)
                #print(new_book)
                db.session.add(new_book)
                db.session.commit()
                return redirect('/admin')
            else:
                return "Section not found"
        
@app.route('/read_book/<int:user_id>/<int:book_id>', methods = ['GET', 'POST'])
def read_book(book_id,user_id):
    this_book = All_books.query.get(book_id)
    user = User.query.get(user_id)
    content = this_book.content
    b_name = this_book.book_name
    return render_template('read_book.html', content = content, u_name = user.user_name, u_id = user.id, b_name = b_name, u_type = 'User')

@app.route('/admin_read_book/<int:book_id>', methods = ['GET', 'POST'])
def admin_read_book(book_id):
    this_book = All_books.query.get(book_id)
    content = this_book.content
    b_name = this_book.book_name
    return render_template('read_book.html', content = content, u_name = 'admin', b_name = b_name, u_type = 'Librarian')

@app.route('/req_book/<int:user_id>/<int:book_id>', methods = ['GET', 'POST'])
def req_book(user_id, book_id):
    user = User.query.get(user_id) 
    book = All_books.query.filter_by(id=book_id).first()
    if len(user.mybooks) >= 5:
        return "You have 5 books, please return a book to borrow another"
    else:
        print(book)
        if request.method == 'POST':
            return_date = request.form.get('date0')
            current_date = datetime.now().date()
            book.user_id = user.id
            book.status = "with the admin"
            book.issue_date = current_date
            book.return_date = return_date
            db.session.commit()
            return redirect(f'/user_dash_allbooks/{user_id}')
        
    reviews = Review.query.filter_by(book_id=book_id).all()
    total_ratings = sum(review.rating for review in reviews)
    num_ratings = len(reviews)
    
    if num_ratings == 0:
        rating=0
    else:
        rating = total_ratings / num_ratings

    return render_template('req_book.html', u_name = user.user_name, u_id = user.id, book = book.id, rating = rating)

@app.route('/libs_user_info/<int:user_id>/<int:book_id>', methods = ['GET', 'POST'])
def libs_user_info(user_id, book_id):
    user = User.query.get(user_id)
    book = All_books.query.filter_by(id=book_id).first()
    u_id = user.id
    u_name = user.user_name
    b_id = book.id
    b_name = book.book_name
    return render_template('libs_user_info.html', u_id = u_id, u_name = u_name, b_id = b_id, b_name = b_name)

@app.route('/download/<int:book_id>/<int:user_id>', methods = ['GET', 'POST'])
def download(book_id, user_id):
    user = User.query.get(user_id)
    book = All_books.query.filter_by(id=book_id).first()
    d_link = book.d_link
    return render_template('download.html', u_name = user.user_name, d_link = d_link, u_id = user.id, book = book.id)

@app.route('/review/<int:user_id>/<int:book_id>', methods = ['GET', 'POST'])
def review(user_id, book_id):
    user = User.query.get(user_id)
    book = All_books.query.filter_by(id=book_id).first()
    return render_template('review.html', u_id = user_id, u_name = user.user_name, book_id = book.id)



#Button Actions

@app.route('/accept_approval/<int:book_id>', methods = ['GET', 'POST'])
def accept_approval(book_id):
    book = All_books.query.filter_by(id=book_id).first()
    book.status = "with user"
    db.session.commit()
    book_apr = All_books.query.filter_by(status='with the admin').all()
    book_given = All_books.query.filter_by(status='with user').all()
    return render_template('book_manage.html', book_apr = book_apr, book_given = book_given)

@app.route('/decline_approval/<int:book_id>', methods = ['GET', 'POST'])
def decline_approval(book_id):
    book = All_books.query.filter_by(id=book_id).first()
    book.status = "in store"
    book.user_id = None
    book.issue_date = None
    book.return_date = None
    db.session.commit()
    book_apr = All_books.query.filter_by(status='with the admin').all()
    book_given = All_books.query.filter_by(status='with user').all()
    return render_template('book_manage.html', book_apr = book_apr, book_given = book_given)

@app.route('/return_book/<int:user_id>/<int:book_id>/<int:rate>', methods = ['GET', 'POST'])
def return_book(book_id, user_id, rate):
    book = All_books.query.filter_by(id=book_id).first()
    book.status = "in store"
    book.user_id = None
    book.issue_date = None
    book.return_date = None
    db.session.commit()
    user = User.query.get(user_id)
    my_books = user.mybooks

    rate = rate
    new_review = Review(book_id = book.id, user_id = user_id, rating = rate)
    db.session.add(new_review)
    db.session.commit()


    return render_template('user_dash_mybooks.html', u_id = user.id, u_name = user.user_name, my_books = my_books)


#search 

@app.route('/search/<int:user_id>')
def text_search(user_id):
    user = User.query.get(user_id)
    srch_word = request.args.get('srch_word')
    srch_word = "%"+raw(srch_word)+"%"
    b_names = All_books.query.filter(All_books.s_book_name.like(srch_word)).all()
    s_authors = All_books.query.filter(All_books.s_author.like(srch_word)).all()
    s_sections = Sections.query.filter(Sections.s_section_name.like(srch_word)).all()
    search_results_book = b_names + s_authors
    search_results_section = s_sections
    return render_template('srch_result.html', u_id = user.id, search_results_book = search_results_book, search_results_section = search_results_section)

def raw(text):
    split_list = text.split()
    src_word = ''
    for word in split_list:
        src_word += word.lower()
    return src_word