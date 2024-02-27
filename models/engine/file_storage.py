#!/usr/bin/python3
"""
serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json


class FileStorage():
    """File Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__] = obj

    def save(self):

        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
