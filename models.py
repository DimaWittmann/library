from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base, init_db


class  User(Base):
        '''
        Represent user record in database
        '''
        __tablename__ = 'user'
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        name = Column(String(50), unique=True)
        password = Column(String(20))
        email = Column(String(120))

        def __init__(self, username=None, password=None, email=None):
                self.name = username
                self.password = password
                self.email = email

        def __repr__(self):
                return "<User ('%s', '%i', '%s')>" %(self.name, self.id, self.password)


class Book_Author(Base):
        __tablename__ = "book_authors"
        __table_args__ = {'autoload': True, 'extend_existing': True,}


class Book(Base):
        __tablename__ = 'book'
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        title = Column(String(50), unique=True)

        def __init__(self, title):
                self.title = title

        def __repr__(self):
                return "<Book ('%s', '%i')>"  %(self.title, self.id)


class Author(Base):
        __tablename__ = 'author'
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        name = Column(String(50), unique=True)

        books = relationship("book", secondary=Book_Author, backref='author')

        def __init__(self, name):
                self.name = name

        def __repr__(self):
                return "<Author ('%s', '%i')>"  %(self.name, self.id)


if __name__ == "__main__":
    init_db()
    