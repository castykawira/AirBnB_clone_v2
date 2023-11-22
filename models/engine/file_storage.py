#!/usr/bin/python3
"""Defines the FileStorage class"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State


class FileStorage:
    """Serializes and deserializes object instances to and from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects of a specific class"""
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}

    def new(self, obj):
        """Associates __objects attribute using key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialization of __objects to JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes __objects from a JSON file if the file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
