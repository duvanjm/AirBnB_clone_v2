#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'Review': Review,
    'User': User,
    'City': City,
    'State': State,
    'Place': Place
}

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
