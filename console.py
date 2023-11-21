#!/usr/bin/python3
"""defines the HBNBCommand class for a basic command interpreter"""
import cmd
import uuid
from datetime import datetime
import os
import re
import shlex
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """defines the command interpreter for the HBNB project"""

    prompt = '(hbnb) '  # if sys.__stdin__.isatty() else ''
    intro = "Welcome to My Command Interpreter. Type 'help' for command"
    classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
            'number_rooms': int, 'number_bathrooms': int,
            'max_guest': int, 'price_by_night': int,
            'latitude': float, 'longitude': float
            }

    def preloop(self):
        """called once before the command loop starts"""
        if sys.__stdin__.isatty():
            print("Welcome to My Command Interpreter. Type 'help' for command")

    def emptyline(self):
        """Overwrites default emptyline method"""
    pass

def precmd(self, line):
    """Refine the command line for advanced syntax to enhance structure"""
    cmd_args = line.split()
    if cmd_args and cmd_args[0] in self.dot_cmds:

            if len(cmd_args) > 1:
                key_value_pairs = [param.split('=') for param in cmd_args[1:]]
                for key, value in key_value_pairs:
                    if key in self.types:
                        try:
                            cmd_args[1] = f"{key}={self.types[key](value)}"
                        except ValueError:
                            print(f"Invalid value for {key}: {value}")
                            return line
            else:
                print("Missing parameters for advanced command syntax.")

                return line

    def do_create(self, arg):
        """Creates new instances of BaseModel with given parameters"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return

        parameters = {}
        for param in args[1:]:
            key_value = param.split('=')
            if len(key_value) == 2:
                key, value = key_value
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ')
                elif '.' in value:
                    value = float(value)
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        print(f"Invalid parameter value: {param}")
                        return

                parameters[key] = value
            else:
                print(f"Invalid parameter format: {param}")
                return

        new_instance = BaseModel(**parameters)

        new_instance.save()

        print(new_instance.id)

    def do_show(self, line):
        """Prints string representation of instances based on class name/id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                print(obj_dict[obj_key])

            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes instances based on class name and id"""
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj_dict = storage.all()
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints string representations of instances based on class name"""
        args = line.split()
        obj_list = []
        obj_dict = storage.all()

        if not args:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        else:
            for key, obj in obj_dict.items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance with a new attribute value"""
    args = line.split()
    if not args:
        print("** class name missing **")
    elif args[0] not in BaseModel.__subclasses__():
        print("** class doesn't exist **")
    elif len(args) < 2:
        print("** instance id missing **")
    else:
        obj_key = args[0] + "." + args[1]
        obj_dict = storage.all()
        if obj_key in obj_dict:
            obj = obj_dict[obj_key]
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    setattr(obj, attr_name, eval(attr_value))
                    obj.save()
                else:
                    print("** attribute doesn't exist **")
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """Exits the console"""
        return True

    def help_quit(self):
        """Exits command-line interpreter"""
        print("Exits command-line interpreter")

    def do_EOF(self, line):
        """Exits console on EOF"""
        print()
        return True

    def help_EOF(self):
        """Print help information for the EOF command"""
        print("Exits the console")

        if __name__ == "__main__":
            HBNBCommand().cmdloop()
