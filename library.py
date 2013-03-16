# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, g, flash, redirect, url_for, jsonify
from forms import RegistrationForm, SigninForm
from database import db_session
from models import User, Book, Author, Book_Author 

DEBUG = True
SECRET_KEY = 'key'
PER_PAGE = 20

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    books = db_session.query(Book).all()
    authors = db_session.query(Author).all()
    if not books:
        books = ["No books have been added",]
    if not authors:
        authors = ["No authors have been added",]
    return render_template('index.html', session=session,\
        books=books, authors=authors)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SigninForm(request.form)
    if request.method == 'POST' and form.validate():

        session["sign_in"] = True
        session["username"] = form.username.data
        "Hello " + session["username"] + "!"
        flash("Hello {user}!".format(user=session["username"]))

        return redirect(url_for('index'))

    return render_template('sign_in.html', form=form)
##
##@app.route('/search', methods=['GET', 'POST'])
##def search():
#
##@app.route('/add_author', methods=['GET', 'POST'])
##def add_author():


@app.route('/sign_out')
def sign_out():
    flash("Good bye")
    session["sign_in"] = False
    return render_template('index.html', session=session)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(username=form.username.data, password=form.password.data, \
                        email=form.email.data)
        db_session.add(new_user)
        db_session.commit()
        flash('Thank you for registering')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
