import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# El ejemplo del diagrama antes de hacerlo se encuentra aqui: mi_diagrama_ejemplo.png

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    home = relationship("home", back_populates="parent")

class Profile(Base):
    __tablename__= "profile"
    id = Column(String(250), primary_key=True)
    user = relationship("user", back_populates="children")
    user_id = Column(Integer, ForeignKey("user.id"))

class Followers(Base):
    __tablename__="followers"
    id = Column(String(250), primary_key=True)
    user = relationship("user", back_populates="children")
    number = Column(String(250), nullable=False)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))

class Following(Base):
    __tablename__="following"
    id = Column(String(250), primary_key=True)
    user = relationship("user", back_populates="children")
    number = Column(String(250), nullable=False)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))

class Direct_message(Base):
    __tablename__="direct_message"
    id = Column(String(250), primary_key=True)
    text = Column(String(250), nullable=False)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))

class Home(Base):
    __tablename__ = 'home'
    id = Column(Integer, primary_key=True)
    user = relationship("user", back_populates="children")
    user_id = Column(Integer, ForeignKey("user.id"))
    user_name=Column(String(250), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url_image = Column(String(250), nullable=False)
    url_video = Column(String(250), nullable=False)
    home_id = Column(Integer, ForeignKey("home.id"))
    home = relationship("home", back_populates="children")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    home_id = Column(Integer, ForeignKey("home.id"))
    home = relationship("home", back_populates="children")
    autor_id = Column(Integer, ForeignKey("user.id"))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')