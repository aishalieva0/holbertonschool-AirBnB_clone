#!/usr/bin/python3
"""Documentation"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs) -> None:
        """Initialization"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if not key == "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value
        if name != "updated_at":
            self.__dict__['updated_at'] = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        result = dict(self.__dict__)
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
