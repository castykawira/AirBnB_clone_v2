#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """Serializes and deserializes object instances to and from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary containing __objects"""
        return self.__objects

    def new(self, obj):
        """Associates __objects attribute using key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialization of __objects to JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes __objects from a JSON file if the file exists"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
