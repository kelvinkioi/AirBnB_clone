#!/usr/bin/python3
""" parent class (called BaseModel) to take care of the
initialization, serialization and deserialization
of your future instances"""
import uuid
from datetime import datetime


class BaseModel:
    """class BaseModel that defines all
    common attributes/methods for other classes"""
    def __init__(self):
        """Class initialization uisng the
        __init__ method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """should print;
        [<class name>] (<self.id>) <self.__dict__>"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        dict_new = self.__dict__.copy()
        dict_new['__class__'] = self.__class__.__name__
        dict_new['created_at'] = self.created_at.isoformat()
        dict_new['updated_at'] = self.updated_at.isoformat()

        return dict_new
