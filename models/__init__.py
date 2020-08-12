#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models.amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()


classes = {
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}
