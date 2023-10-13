#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    Test_user
"""
import unittest
from models.user import User


class Test_places(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        user.email = "Test email"
        user.password= "Test password"
        user.first_name = "Test first_name"
        user.last_name = "Test last_name"
       
       
       
        self.assertEqual(user.email, "Test email")
        self.assertEqual(user.password, "Test password")
        self.assertEqual(user.first_name, "Test first_name")
        self.assertEqual(user.last_name, "Test last_name")

if __name__ == "__main__":
    unittest.main()
