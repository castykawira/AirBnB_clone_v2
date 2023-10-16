#!/usr/bin/python3i
"""The definition of the HBnB console."""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Handle default command processing."""
        cmd_tokens = arg.split()
        if len(cmd_tokens) == 0:
            return False
        cmd_name = cmd_tokens[0]
        class_name = None
        if len(cmd_tokens) > 1:
            class_name = cmd_tokens[1]

        if cmd_name == "create":
            self.do_create(class_name)
        elif cmd_name == "show":
            if len(cmd_tokens) >= 3:
                self.do_show(f"{class_name} {cmd_tokens[2]}")
        elif cmd_name == "destroy":
            if len(cmd_tokens) >= 3:
                self.do_destroy(f"{class_name} {cmd_tokens[2]}")
        elif cmd_name == "all":
            if len(cmd_tokens) >= 2:
                self.do_all(class_name)
        elif cmd_name == "update":
            if len(cmd_tokens) >= 5:
                self.do_update(f"{class_name} {cmd_tokens[2]} {cmd_tokens[3]} {cmd_tokens[4]}")
        else:
            print(f"*** Unknown syntax: {arg}")
        return False

    def do_create(self, arg):
        """Usage: create <class_name>
        Create a new instance of the specified class, save it, and print its ID.
        """
        if arg and arg in BaseModel.__subclasses__():
            new_instance = BaseModel.__subclasses__[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Usage: show <class_name> <id>
        Print the string representation of an instance based on the class name and ID.
        """
        if arg:
            args = arg.split()
            if len(args) == 2 and args[0] in BaseModel.__subclasses__():
                objects = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
            else:
                print("** class name missing **" if len(args) < 1 else "** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Usage: destroy <class_name> <id>
        Delete an instance based on the class name and ID.
        """
        if arg:
            args = arg.split()
            if len(args) == 2 and args[0] in BaseModel.__subclasses__():
                objects = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class name missing **" if len(args) < 1 else "** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Usage: all [class_name]
        Print all string representations of instances (or instances of the specified class).
        """
        args = arg.split()
        objects = storage.all()
        obj_list = []

        if args and args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        else:
            for key, obj in objects.items():
                if not args or key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        Update an instance's attribute based on the class name and ID.
        """
        args = arg.split()
        if len(args) >= 4 and args[0] in BaseModel.__subclasses__():
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
        else:
            print("** class name missing **" if len(args) < 1 else "** instance id missing **

