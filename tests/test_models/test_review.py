#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    Test_review
"""
import unittest
from models.review import Review


class Test_places(unittest.TestCase):
    def test_place_attributes(self):
        review = Review()
        review.place_id = "test_place_id"
        review.user_id = "test_user_id"
        review.text = "Test review"
       
        
        self.assertEqual(review.place_id, "test_place_id")
        self.assertEqual(review.user_id, "test_user_id")
        self.assertEqual(review.text, "Test review")

if __name__ == "__main__":
    unittest.main()
