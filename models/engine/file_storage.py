#!/usr/bin/python3
'''module: file_storage
'''

import json
import os

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
        objects_dict = {ky: val.to_dict() for ky, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

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

    
