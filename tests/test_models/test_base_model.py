#!/usr/bin/python3
"""
unittest for base module
"""


import unittest
from models.base_model import BaseModel
from os import path


class Test_BaseModel(unittest.TestCase):
    """ test for BaseModel class """
    def test_init(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.created_at)

    def test_save(self):
        obj = BaseModel()
        obj.save()
        self.assertTrue(path.isfile("file.json"))
        with open('file.json') as f:
            self.assertIn("BaseModel." + obj.id , f.read())

    def test_str(self):
        obj = BaseModel()
        self.assertIn(obj.id, str(obj))

if __name__ == '__main__':
    unittest.main()
