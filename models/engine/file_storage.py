#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes object instances to and from a JSON file"""

    def all(self):
        """Returns the dictionary containing __objects"""
        return FileStorage.__objects

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
