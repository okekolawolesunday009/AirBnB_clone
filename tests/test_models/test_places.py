#!/usr/bin/python3
"""Defines unittests for models/places.py.
Unittest classes:
    Test_places
"""
import unittest
from models.place import Place


class Test_places(unittest.TestCase):
    def test_place_attributes(self):
        place = Place()
        place.city_id = "test_city_id"
        place.user_id = "test_user_id"
        place.name = "Test Place"
        place.description = "Test description"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_id = ["amenity1", "amenity2"]
        
        self.assertEqual(place.city_id, "test_city_id")
        self.assertEqual(place.user_id, "test_user_id")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Test description")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_id, ["amenity1", "amenity2"])


if __name__ == "__main__":
    unittest.main()
