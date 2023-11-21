#!/usr/bin/python3
"""unit test module for the HBNBCommand class in console.py"""
import unittest
from unittest.mock import patch
import json
import MySQLdb
import os
import re
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', return_value='create BaseModel name="My House" number=42\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Generated ID\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', return_value='show BaseModel 1234-5678\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Output of show command\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        with patch('builtins.input', return_value='destroy BaseModel 1234-5678\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Output of destroy command\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        with patch('builtins.input', return_value='all BaseModel\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Output of all command\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_command(self, mock_stdout):
        with patch('builtins.input', return_value='update BaseModel 1234-5678 name="New House"\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Output of update command\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value='quit\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Exits command-line interpreter\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        with patch('builtins.input', return_value='EOF\n'):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), 'Exits the console\n')


if __name__ == '__main__':
    unittest.main()
