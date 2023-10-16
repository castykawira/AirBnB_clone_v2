#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    intro = "Welcome to My Command Interpreter. Type 'help' for a list of available commands."
    prompt = "(hbnb) "

    def do_hello(self, line):
        """Print a greeting message"""
        if line:
            print("Hello, " + line)
        else:
            print("Hello, World!")

    def do_quit(self, line):
        """Exit the command interpreter"""
        return True

    def help_hello(self):
        print("Print a greeting message. Usage: hello [name]")

    def help_quit(self):
        print("Exit the command interpreter.")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

