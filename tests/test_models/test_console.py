#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    Test_console
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand  # Replace 'your_module_name' with the actual module name

class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        self.hbnb = HBNBCommand()
    
    def tearDown(self):
        self.hbnb = None

    def test_create(self):
        with patch('builtins.input', side_effect=['create User']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb.onecmd('create User')
                output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith('User.'))

    def test_show(self):
        # Test show with an existing instance
        with patch('builtins.input', side_effect=['create User']):
            self.hbnb.onecmd('create User')
        with patch('builtins.input', side_effect=['show User 1']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb.onecmd('show User 1')
                output = mock_stdout.getvalue().strip()
        self.assertTrue('User' in output)

        # Test show with a non-existent instance
        with patch('builtins.input', side_effect=['show User 2']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb.onecmd('show User 2')
                output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** no instance found **')

        # Test show with missing instance ID
        with patch('builtins.input', side_effect=['show User']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.hbnb.onecmd('show User')
                output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** instance id missing **')

    # Write similar test methods for other commands (destroy, all, update)

if __name__ == '__main__':
    unittest.main()
