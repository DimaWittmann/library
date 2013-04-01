# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, g, flash, redirect,\
                  url_for, jsonify
from forms import RegistrationForm, SigninForm, AddBookForm, AddAuthorForm, \
                  UpdateBookForm, UpdateAuthorForm
from database import db_session
from models import User, Book, Author

DEBUG = True
SECRET_KEY = 'key'
PER_PAGE = 20

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    authors = db_session.query(Author).all()
    books = db_session.query(Book).all()

    return render_template('index.html', session=session,\
                           books=books, authors=authors)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SigninForm(request.form)
    if request.method == 'POST' and form.validate():
        session["sign_in"] = True
        session["username"] = form.username.data
        flash("Hello {user}!".format(user=session["username"]))
        return redirect(url_for('index'))

    return render_template('sign_in.html', form=form)


@app.route('/sign_out')
def sign_out():
    flash("Good bye {user}!".format(user=session["username"]))
    session["sign_in"] = False
    authors = db_session.query(Author).all()
    books = db_session.query(Book).all()
    return render_template('index.html', session=session,\
                           books=books, authors=authors)


@app.route('/book/<int:bID>', methods=['GET', 'POST', 'DELETE'])
def book(bID):
    form = UpdateBookForm(request.form)
    authors = db_session.query(Author).all()
    form.authors.choices = [(i, authors[i - 1]) for i in xrange(1, len(authors) + 1)]
    selected_book = Book.query.filter(Book.id == bID).one()

    if request.method == 'GET':
        authors = selected_book.authors
        return render_template("book.html", authors=authors, \
               book=selected_book, form=form)
    elif request.method == 'POST' and form.validate():
        book = Book.query.filter(Book.id == bID).one()
        book.title = form.new_title.data
        authors = request.form.getlist('authors')
        authors = Author.query.filter(Author.id.in_(authors)).all()
        for author in authors:
            if author in book.authors:
                book.authors.remove(author)
            else:
                book.authors.append(author)
        db_session.commit()
        return redirect(url_for("book", bID=bID))


@app.route('/author/<int:aID>', methods=['GET', 'POST', 'DELETE'])
def author(aID):
    form = UpdateAuthorForm(request.form)
    selected_author = Author.query.filter(Author.id == aID).one()
    books = Book.query.all()
    form.books.choices = [(i, books[i - 1]) for i in xrange(1, len(books) + 1)]
    if request.method == 'GET':
        books = selected_author.books
        return render_template("author.html", books=books,\
               author=selected_author, form=form)
    elif request.method == 'POST' and form.validate():
        author = Author.query.filter(Author.id == aID).one()
        author.name = form.new_name.data
        books = request.form.getlist('books')
        books = Book.query.filter(Book.id.in_(books)).all()
        for book in books:
            if book in author.books:
                author.books.remove(book)
            else:
                author.books.append(book)
        db_session.commit()
        return redirect(url_for("author", aID=aID))

@app.route('/add_entity', methods=['GET', ])
def add_entity():
    forms = {
            "new_book": AddBookForm(),
            "new_author": AddAuthorForm()
           }
    return render_template('add_entity.html', form=forms)


@app.route('/add_entity/book', methods=['POST', ])
def add_book():
    form = AddBookForm(request.form)
    if form.validate():
        new_book = Book(form.title.data)
        db_session.add(new_book)
        db_session.commit()
        flash('{book} is added'.format(book=form.title.data))
    else:
        forms = {
            "new_book": form,
            "new_author": AddAuthorForm()
           }
        return render_template('add_entity.html', form=forms)
    return redirect(url_for("add_entity"))


@app.route('/add_entity/author', methods=['POST', ])
def add_author():
    form = AddAuthorForm(request.form)
    if form.validate():
        new_author = Author(form.name.data)
        db_session.add(new_author)
        db_session.commit()
        flash('{author} is added'.format(author=form.name.data))
    else:
        forms = {
            "new_book": AddBookForm(),
            "new_author": form
           }
        return render_template('add_entity.html', form=forms)
    return redirect(url_for("add_entity"))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(username=form.username.data, password=form.password.data,\
                        email=form.email.data)
        db_session.add(new_user)
        db_session.commit()
        flash('Thank you for registering')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
