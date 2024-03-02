#!/usr/bin/python3
"""User tests"""


import unittest
import os

from models.user import User
from models import storage


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.usr = User()

    def test_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        self.usr.email = "hey@gmail.com"
        self.assertEqual(self.usr.email, "hey@gmail.com")

    def test_passwd(self):
        self.usr.password = "123"
        self.assertEqual(self.usr.password, "123")
    
    def test_first_name(self):
        self.usr.first_name = "Saleh"
        self.assertEqual(self.usr.first_name, "Saleh")

    def test_last_name(self):
        self.usr.last_name = "Abbas"
        self.assertEqual(self.usr.last_name, "Abbas")
