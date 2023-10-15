#!/usr/bin/python3
"""Defines the BaseModel class within this module"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """provides shared attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Creates a new instance of the BaseModel class

        Args:
            *args: Variable length positional arguments
            **kwargs: Variable length keyword arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime
                    (value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Produces a string representation of the BaseModel instance

        Returns:
            str: String representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Produces a dictionary with all keys/values from the instance's __dict__

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
