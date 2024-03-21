#!/usr/bin/python3
"""Module init for models module"""
from os import getenv
from .base_model import BaseModel

name2class = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Review": Review
}

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
