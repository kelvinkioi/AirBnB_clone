#!/usr/bin/python3
'''module: file_storage
'''

import json
import os
import datetime


class FileStorage:
    '''serializes/deserializes to JSON file

        Attributes:
            __file_path (str): path to JSON file
            __object (dict) : stores all objects
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects with key<obj class name>.id
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''serialization
        '''
        od = {ky: val.to_dict() for ky, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(od, file)

    def reload(self):
        '''deserialization
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            loaded = json.load(file)
            loaded = {key: self.classes()[value["__class__"]](**value)
                      for key, value in loaded.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = loaded

    def classes(self):
        '''returns a dictionary mapping
            class names to their corresponding classes
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def attributes(self):
        '''returns the valid attributes and their
            types for classname
        '''
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
