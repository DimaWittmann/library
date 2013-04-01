from wtforms import Form,  TextField, PasswordField, validators, SelectMultipleField
from validators import UniqueValidator, ExistsValidator, PasswordValidator
from models import User, Book, Author
from database import db_session


class RegistrationForm(Form):
    username = TextField("Login", [validators.required("Please enter login"), \
                    UniqueValidator(db_session, User, User.name)])

    email = TextField("email", [validators.required("Please enter email"), \
                    validators.email("Please enter valid email")])

    password = PasswordField("Password", [validators.Required("Please enter password"), \
                    validators.EqualTo("confirm", message="Passwords do not match")])

    confirm = PasswordField("Confirm")


class SigninForm(Form):
    username = TextField("Login", [validators.required("Please enter login"),\
                    ExistsValidator(db_session, User, User.name)])

    password = PasswordField("Password", [validators.Required("Please enter password"),\
                    PasswordValidator(db_session)])


class AddBookForm(Form):
    title = TextField("Title", [validators.required("Please enter title"),\
                    UniqueValidator(db_session, Book, Book.title)])


class AddAuthorForm(Form):
    name = TextField("Author", [validators.required("Please enter name"),\
                    UniqueValidator(db_session, Author, Author.name)])


class UpdateBookForm(Form):
    new_title = TextField("New title")
    authors = SelectMultipleField('Authors', coerce=int)


class UpdateAuthorForm(Form):
    new_name = TextField("New name")
    books = SelectMultipleField('Books', coerce=int)
