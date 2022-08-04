import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# El ejemplo del diagrama antes de hacerlo se encuentra aqui: mi_diagrama_ejemplo.png

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False)
    phone_number = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(80), nullable=False)
    Address = Column(String(150), nullable=False)
    is_active = Column(Boolean(), nullable=False)
    comment = relationship("Comment", back_populates="user")
    favorite_books = relationship("FavoriteBooks", back_populates="user")

class FavoriteBooks(Base):
    __tablename__ = 'favorite_books'
    id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="favorite_books")
    user_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", back_populates="favorite_books")

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    rating = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    authors = Column(String(250), nullable=False)
    cover = Column(String(250), nullable=False)
    year = Column(String(250), nullable=False)
    favorite_books = relationship("FavoriteBooks", back_populates="book")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="comment")
    user_id = Column(Integer, ForeignKey("user.id"))
    user_name = Column(String(120), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"))
    content = Column(String(250), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')