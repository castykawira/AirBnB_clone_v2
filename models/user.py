#!/usr/bin/python3
"""This module defines the User class"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """this class defines the User class"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade="all,delete", backref="user")
        reviews = relationship('Review', cascade="all,delete", backref="user")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """Set the password for the user"""
        self._password = pwd
