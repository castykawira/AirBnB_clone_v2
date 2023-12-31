#!/usr/bin/python3
"""This module defines the State class"""
from models.city import City
from os import getenv
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This class defines the State class"""
    if storage_type == "db":
         __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter method to return the list of City objects"""
            citiesList = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList
