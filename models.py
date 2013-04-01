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


Book_Author = Table("book_authors", Base.metadata,
                Column('author_id', Integer, ForeignKey('author.id')),
                Column('book_id', Integer, ForeignKey('book.id'))
                )


class Book(Base):
        __tablename__ = 'book'
        id = Column(Integer, primary_key=True)
        title = Column(String(50), unique=True)

        def __init__(self, title):
                self.title = title

        def __repr__(self):
                return "%s" % (self.title)


class Author(Base):
        __tablename__ = 'author'
        id = Column(Integer, primary_key=True)
        name = Column(String(50), unique=True)

        books = relationship("Book", secondary="book_authors", backref='authors')

        def __init__(self, name):
                self.name = name

        def __repr__(self):
                return "%s" % (self.name,)

init_db()
