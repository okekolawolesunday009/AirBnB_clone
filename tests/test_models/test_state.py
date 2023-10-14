#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    Test_state
"""
import unittest
from models.state import State


class Test_places(unittest.TestCase):
    def test_place_attributes(self):
        state = State()
        state.name = "Test state"
       
       
       
        self.assertEqual(state.name, "Test state")

if __name__ == "__main__":
    unittest.main()
