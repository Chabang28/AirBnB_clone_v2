#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place',
                          cascade='all, delete',
                          backref='user')
    reviews = relationship('Review',
                           cascade='all, delete',
                           backref='user')
