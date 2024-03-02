#!/usr/bin/python3
"""City Testing Model"""


import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.state_id = "062"
        self.city.name = "Zaqatala"

    def test_type(self):
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

    def test_id(self):
        self.assertEqual(self.city.state_id, "062")

    def test_name(self):
        self.assertEqual(self.city.name, "Zaqatala")
