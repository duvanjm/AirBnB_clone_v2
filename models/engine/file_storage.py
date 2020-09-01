#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            objects = {}
            for key, val in FileStorage.__objects.items():
                class_ = key.split('.')
                if cls.__name__ == class_[0]:
                    objects[key] = val
            return objects

        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    """ def save(self):
        a_dict = {}
        for key in self.__objects:
            a_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w",
                  encoding="utf-8") as a_file:
            json.dump(a_dict, a_file) """

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Remove object from a stored file """

        if obj is not None:
            temp = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects.pop(temp, None)
            FileStorage.save(self)

    def close(self):
        """call reload() method for deserializing
        the JSON file to objects"""
        FileStorage.reload(self)
