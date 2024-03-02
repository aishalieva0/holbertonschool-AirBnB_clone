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
            os.remove(self.file_storage.__file_path)
        except IOError:
            pass

    def test_all(self):
        self.assertEqual(self.file_storage.all(), {})

