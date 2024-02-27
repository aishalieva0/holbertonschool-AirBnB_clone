#!/usr/bin/python3
"""
serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage():
    __file_path = ""
    __objects = {}

    def all(self):

