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

    def test_dict(self):
        obj = BaseModel()
        obj_d = obj.to_dict()

        self.assertIsInstance(obj_d, dict)
        self.assertEqual(obj_d['id'], obj.id)
        self.assertEqual(obj_d['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_d['updated_at'], obj.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
