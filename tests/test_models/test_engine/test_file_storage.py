import json
import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.file_storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self) -> None:
        try:
            os.remove(self.file_storage._FileStorage__file_path)
        except IOError:
            pass

    def test_all(self):
        print(self.file_storage.all())
        self.assertEqual(len(self.file_storage.all()), 1)

