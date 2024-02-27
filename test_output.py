#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

base_model = BaseModel()
base_model.name = "Test Model"
base_model.value = 123

storage = FileStorage()
storage.new(base_model)
storage.save()

storage.reload()
# After reloading objects
reloaded_objects = storage.all()
reloaded_base_model = reloaded_objects.get(f"BaseModel.{base_model.id}")

if reloaded_base_model:
    # Print attributes of original object
    print("Original object attributes:", base_model.__dict__)
    # Print attributes of reloaded object
    print("Reloaded object attributes:", reloaded_base_model.__dict__)

    # Check if attributes match
    attributes_match = (
        reloaded_base_model.name == base_model.name
        and reloaded_base_model.value == base_model.value
    )
    print("Attributes match:", attributes_match)
else:
    print("Reloaded object not found")

