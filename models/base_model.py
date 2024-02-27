#!/usr/bin/python3
"""
defines all common attributes/methods
"""


import uuid
from datetime import datetime


class BaseModel():
    """  Base model """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def __setattr__(self, attr_name, attr_val):
        """ ... """
        if attr_name != ["updated_at"]:
            self.__dict__["update_at"] = datetime.now()

        self.__dict__[attr_name] = attr_val

    def save(self):
        """ ... """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ ... """
        result = self.__dict__
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

