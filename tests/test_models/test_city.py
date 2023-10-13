#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    Test_city
"""
import unittest
from models.city import City


class Test_places(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        city.state_id = "test_city_id"
        city.name = "Test City"
        
        self.assertEqual(city.state_id, "test_city_id")
        self.assertEqual(city.name, "Test City")


if __name__ == "__main__":
    unittest.main()
