#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
# Create and save objects
obj1 = BaseModel(name='Object 1')
obj2 = BaseModel(name='Object 2')

# Save objects to JSON file
storage.save()

# Reload objects
storage.reload()

# Retrieve reloaded objects from storage
reloaded_objects = storage.all()

# Compare attributes of original objects with reloaded objects
for obj_id, original_obj in reloaded_objects.items():
    reloaded_obj = storage.all().get(obj_id)
    if reloaded_obj:
        assert original_obj.name == reloaded_obj.name

# If the assertions pass, it means that the reloaded objects have the same attributes as the original objects.
print("Test passed: Reloaded objects are the same as created objects.")

