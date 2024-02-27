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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        print(obj_dict)
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        data = {} 
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
            FileStorage.__objects = data
        except FileNotFoundError:
            pass
